from appuser.api.serializers import User
from django.contrib import admin
# from knox import views as knox_views
from django.urls import path
from .views import UserCreateAPIView
urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='apisregister'),
]
