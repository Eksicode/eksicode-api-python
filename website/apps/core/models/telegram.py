from django.db import models

from .base import Base


class TelegramGroup(Base):
    # Informational
    name = models.CharField(max_length=100)
    group_id = models.CharField(blank=True, null=True, max_length=100)
    user_count = models.IntegerField(default=0)

    # Configurable
    icon = models.ImageField()
    description = models.TextField(blank=True, null=True)
