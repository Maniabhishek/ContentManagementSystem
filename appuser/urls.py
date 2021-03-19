from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import register, loginAccount

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', loginAccount, name='loggin'),

]
