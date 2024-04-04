from rest_framework import serializers
from ..models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer (serializers.ModelSerializer) : 
    password = serializers.CharField(write_only=True,validators=[validate_password])

    class Meta:
        model = User
        fields = ('id',"full_name",'email','password','picture')
        
    def save(self, **kwargs):
        user = User.objects.create_user(**self.validated_data)
        user.save()
        
        return user

