from channels.generic.websocket import WebsocketConsumer
from ..models import Battle

class BattleConsumer (WebsocketConsumer) : 

    def connect(self):
        self.user = self.scope['user']
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        
        try : 
            self.battle = Battle.objects.get(id=self.room_id)
        except Exception:
            self.close()
            return
        
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data):
        print(text_data, type(text_data))