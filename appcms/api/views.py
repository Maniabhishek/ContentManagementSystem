from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions, request
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from appcms.api.permissions import IsOwnerOrReadOnly
from rest_framework import response
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView, RetrieveUpdateAPIView)
from .serializers import (
    ContentSerializer, ContentUpdateSerializer, ContentCreateSerializer)
from appcms.models import Content
from rest_framework import serializers
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from appuser.models import Profile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from .permissions import IsOwnerOrReadOnly

# this is for searching purpose this can let you search in content list based on different fields


class ContentFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr='icontains')
    body = filters.CharFilter(field_name="body", lookup_expr='icontains')
    summary = filters.CharFilter(field_name="summary", lookup_expr='icontains')
    category = filters.NumberFilter(
        field_name="category", lookup_expr='icontains')
    author = filters.CharFilter(
        field_name="author__username", lookup_expr='icontains')

    class Meta:
        model = Content
        fields = ['title', 'body', 'summary', 'category', 'author']

# this is listing down all the contents


class ContentListAPIView(ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContentFilter

# ContentDetailAPIView list details of one  particular content


class ContentDetailAPIView(RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

# this is for updating contents and only for logged in user and the owner of the content


class ContentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

# this is for deleting contents and only for logged in user and the owner of the content


class ContentDeleteAPIView(DestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# this view is for creating the content and only allows


class ContentCreateView(CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        content = Content(author=self.request.user)
        serializer = ContentCreateSerializer(content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
