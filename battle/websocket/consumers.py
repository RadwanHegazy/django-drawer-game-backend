from channels.generic.websocket import WebsocketConsumer
from ..models import Battle
from users.models import User
import json
from asgiref.sync import async_to_sync


class BattleConsumer (WebsocketConsumer) : 

    def connect(self):
        self.user:User = self.scope['user']
        self.room_id = self.scope['url_route']['kwargs']['room_id']

        self.fired = False
        try : 
            self.battle = Battle.objects.get(id=self.room_id)
        except Exception:
            self.fired = True
            self.close()
            return
        
        self.ROOM_NAME = f'room_{self.room_id}'
        self.accept()
        
        async_to_sync(self.channel_layer.group_add)(
            self.ROOM_NAME,
            self.channel_name,
        )

        async_to_sync(self.channel_layer.group_send)(
            self.ROOM_NAME,
            {
                'type':'join',
                'username':self.user.full_name
            }
        )
        
        

    def disconnect(self, code):
        
        if not self.fired : 
            async_to_sync(self.channel_layer.group_send)(
                self.ROOM_NAME,
                {
                    'type':'leave',
                    'username':self.user.full_name
                }
            )
            
            async_to_sync(self.channel_layer.group_discard)(
                self.ROOM_NAME,
                self.channel_name,
            )


    def receive(self, text_data):
        json_data:dict = json.loads(text_data)
        msg_type = json_data.get('type',None)
        
        if msg_type == 'msg' :
            custom_data = {
                'sender' : self.user.full_name,
                'sender_id':self.user.id,
                'body':json_data['data']['body']
            }
            json_data['data'] = custom_data
            async_to_sync(self.channel_layer.group_send)(


                self.ROOM_NAME,
                {
                    'type':'gameplay',
                    'data':json.dumps(json_data)
                }
            )

        owner_types = ['add','remove_all','win']
        if msg_type in owner_types and self.user == self.battle.owner :
            async_to_sync(self.channel_layer.group_send)(
                self.ROOM_NAME,
                {
                    'type':'gameplay',
                    'data':json.dumps(json_data)
                }
            )

            if msg_type == 'win' : 
                self.battle.delete()
                self.close()
                return

    def join(self,username) :
        data = {
            'type' : 'join',
            'username' : username['username']
        }
        self.send(text_data=json.dumps(data))
    
    def leave(self,username) :
        data = {
            'type' : 'leave',
            'username' : username['username']
        }
        self.send(text_data=json.dumps(data))
    
    def gameplay (self,data):
        self.send(text_data=data['data'])