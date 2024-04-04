from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from users.apis.serializers import RegisterSerializer

class UserRegisterView (CreateAPIView) : 
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

