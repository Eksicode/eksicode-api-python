from django.contrib import admin

from .base import BaseModelAdmin
from ..models import TrafficMeta


@admin.register(TrafficMeta)
class TrafficMetaAdmin(BaseModelAdmin):
    ...
