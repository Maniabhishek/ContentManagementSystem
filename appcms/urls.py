from django.urls import path
from .views import ContentListView, ContentDetailView, ContentCreateView, ContentUpdateView, ContentDeleteView, Search

urlpatterns = [
    path('', ContentListView, name='home'),
    path('content/<int:pk>/', ContentDetailView.as_view(), name='contentDetail'),
    path('content/new/', ContentCreateView.as_view(), name='contentCreate'),
    path('content/<int:pk>/update',
         ContentUpdateView.as_view(), name='contentUpdate'),
    path('content/<int:pk>/delete',
         ContentDeleteView.as_view(), name='contentDelete'),

]
