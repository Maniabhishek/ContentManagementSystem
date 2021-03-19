from rest_framework.serializers import ModelSerializer
from appcms.models import Content


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'author', 'title',
                  'body', 'summary', 'category', 'pdf']


class ContentUpdateSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'body', 'summary', 'category']


class ContentCreateSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'body', 'summary', 'category', 'pdf']
