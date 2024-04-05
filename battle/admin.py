from django.contrib import admin
from .models import Battle


@admin.register(Battle)
class BattlePanel(admin.ModelAdmin) : 
    list_display = ['id','owner']