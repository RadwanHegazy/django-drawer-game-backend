from django.contrib import admin
from django.urls import path, include
from backend import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include('users.apis.urls')),
    path('api/battle/',include('battle.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
