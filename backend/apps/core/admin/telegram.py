from django.contrib import admin

from .base import BaseModelAdmin
from ..models import TelegramGroup


@admin.register(TelegramGroup)
class TelegramGroupAdmin(BaseModelAdmin):
    ...
