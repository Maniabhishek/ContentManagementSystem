from django.contrib import admin
from django.urls import path
from .views import (ContentListAPIView, ContentDetailAPIView,
                    ContentUpdateAPIView, ContentDeleteAPIView, ContentCreateView)
urlpatterns = [
    path('', ContentListAPIView.as_view(), name='apiHome'),
    path('content/<int:pk>/', ContentDetailAPIView.as_view(), name='contentDetail'),
    path('content/<int:pk>/update',
         ContentUpdateAPIView.as_view(), name='contentUpdate'),
    path('content/<int:pk>/delete',
         ContentDeleteAPIView.as_view(), name='contentDelete'),
    path('content/create', ContentCreateView.as_view(), name='contentCreate'),




]
