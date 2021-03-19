from django.db.models import fields
from .models import Content
import django_filters


class ContentFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    body = django_filters.CharFilter(lookup_expr='icontains')
    summary = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Content
        fields = ['title', 'body', 'summary', 'category']
