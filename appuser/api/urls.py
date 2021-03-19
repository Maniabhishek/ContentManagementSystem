from appuser.api.serializers import User
from django.contrib import admin
# from knox import views as knox_views
from django.urls import path
from .views import UserCreateAPIView
urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='apisregister'),
    # path('login/', LoginAPIView.as_view(), name='apislogin'),
    # path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
