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
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from .permissions import IsOwnerOrReadOnly


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


class ContentListAPIView(ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = [DjangoFilterBackend]
    # search_fields = ['title', 'body', 'summary', 'category', 'author']
    filterset_class = ContentFilter
    # def get_queryset(self, *args, **kwargs):
    #     if 'q' in self.request.GET and self.request.GET['q']:
    #         q = self.request.GET['q']
    #         queryset = Content.objects.filter(title__icontains=q)
    #     else:
    #         queryset = Content.objects.all()
    #     return queryset


class ContentDetailAPIView(RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ContentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class ContentDeleteAPIView(DestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ContentCreateView(CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # profile = User.objects.get(pk=1)
        content = Content(author=self.request.user)
        serializer = ContentCreateSerializer(content, data=request.data)
        # data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
