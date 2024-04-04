from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

class ProfileView (APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request) : 
        user = request.user
        data = {
            'full_name' : user.full_name,
            'email' : user.email,
            'picture' : user.picture.url,
        }
        return Response(data,status=status.HTTP_200_OK)