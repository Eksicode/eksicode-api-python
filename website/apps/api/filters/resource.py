from django_filters import rest_framework as filters

from apps.core.models import Resource
from .base import TagFilter


class ResourceFilter(filters.FilterSet):
    tags = TagFilter(field_name='tags__name')

    class Meta:
        model = Resource
        fields = {
            'approved': ['exact']
        }
