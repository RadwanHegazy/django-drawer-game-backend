from django.db import models
from uuid import uuid4
from django.core.exceptions import ValidationError



class Battle (models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid4)
    owner = models.ForeignKey('users.User',related_name='battle_owner',on_delete=models.CASCADE)
    guests = models.ManyToManyField('users.User',related_name='guests_battle')
