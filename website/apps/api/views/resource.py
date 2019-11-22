from rest_framework.viewsets import ModelViewSet

from apps.core.models import Resource
from ..serializer import ResourceSerializer


class ResourceViewSet(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
