from rest_framework.viewsets import ModelViewSet

from apps.core.models import TelegramGroup
from ..serializers import TelegramGroupSerializer


class TelegramGroupViewSet(ModelViewSet):
    serializer_class = TelegramGroupSerializer

    def get_queryset(self):
        return TelegramGroup.objects.all()
