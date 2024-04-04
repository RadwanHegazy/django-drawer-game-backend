from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import register, profile

urlpatterns = [
    path('login/',TokenObtainPairView.as_view()),
    path('register/',register.UserRegisterView.as_view()),
    path('profile/',profile.ProfileView.as_view()),
]