from rest_framework.viewsets import ModelViewSet

from apps.core.models import Resource
from ..serializer import ResourceSerializer


class ResourceViewSet(ModelViewSet):
    serializer_class = ResourceSerializer

    def get_queryset(self):
        return Resource.objects.all()
