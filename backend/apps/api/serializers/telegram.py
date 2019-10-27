from rest_framework import serializers

from apps.core.models import TelegramGroup


class TelegramGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramGroup
        fields = [
            'id',
            'created_at',
            'last_updated_at',
            'name',
            'group_id',
            'user_count',
            'icon',
            'description',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'last_updated_at',
        ]
