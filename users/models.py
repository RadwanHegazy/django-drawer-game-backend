from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser

class User (AbstractUser) : 
    """Custom user model in the system"""
    objects = CustomUserManager()
    
    username = None
    groups = None
    user_permissions = None
    first_name = None
    last_name = None

    full_name = models.CharField(max_length=225)
    picture = models.ImageField(upload_to='user-pics/',default='user.png')
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['full_name']
    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.full_name