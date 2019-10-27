from rest_framework.viewsets import ModelViewSet

from apps.core.models import Resource
from .base import custom_paginator
from ..filters import ResourceFilter
from ..serializers import ResourceSerializer


class ResourceViewSet(ModelViewSet):
    serializer_class = ResourceSerializer
    filterset_class = ResourceFilter
    ordering_fields = ['created_at', 'name']
    pagination_class = custom_paginator()

    def get_queryset(self):
        return Resource.objects.all()
