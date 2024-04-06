from django.urls import path
from .views import create, get

urlpatterns = [
    path('create/',create.CreateBattle.as_view()),
    path('get/<str:battle_id>/',get.GetBattle.as_view()),
]