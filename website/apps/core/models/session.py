from django.db import models
from django.contrib.auth.models import User


class Sessions(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    session_date = models.DateTimeField()
    ip_address = models.GenericIPAddressField()
    os = models.TextField()
    browser = models.TextField()
    device = models.TextField(blank=True, null=True)
