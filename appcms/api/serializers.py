from rest_framework.serializers import ModelSerializer
from appcms.models import Content

# for listing all the contents


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'author', 'title',
                  'body', 'summary', 'category', 'pdf']

# for updating the content


class ContentUpdateSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'body', 'summary', 'category', 'pdf']

# this is for creatign the contents


class ContentCreateSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'body', 'summary', 'category', 'pdf']
