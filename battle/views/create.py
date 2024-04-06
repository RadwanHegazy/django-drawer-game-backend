from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from ..models import Battle


class CreateBattle(APIView) : 
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request) :
        user = request.user
        battle = Battle.objects.create(
            owner=user
        )
        battle.save()
        data = {
            'id' : str(battle.id)
        }
        return Response(data,status=status.HTTP_201_CREATED)
