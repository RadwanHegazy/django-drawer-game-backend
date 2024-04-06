from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from ..models import Battle


class GetBattle(APIView) : 
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,battle_id) :
        user = request.user

        try : 
            battle = Battle.objects.get(id=battle_id)
        except Exception :
            return Response({
                'message' : 'battle not exist'
            },status=status.HTTP_404_NOT_FOUND)
        
        if user != battle.owner and user not in battle.guests.all(): 
            battle.guests.add(user)
        data = {
            'id' : str(battle.id),
            'owner' : battle.owner.id
            # 'guests' : [i.id for i in battle.guests.all()],
        }
        return Response(data,status=status.HTTP_200_OK)
