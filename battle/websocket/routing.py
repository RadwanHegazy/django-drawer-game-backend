from django.urls import path
from .consumers import BattleConsumer

ws_urlpatterns = [
    path('ws/battle/<str:room_id>/',BattleConsumer.as_asgi()),
]