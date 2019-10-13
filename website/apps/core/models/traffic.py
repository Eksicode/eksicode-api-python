from django.db import models

from .base import Base


class TrafficMeta(Base):
    user = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    os = models.CharField(max_length=100, default='UNKNOWN')
    browser = models.CharField(max_length=100, default='UNKNOWN')
    device = models.CharField(max_length=100, default='UNKNOWN')
