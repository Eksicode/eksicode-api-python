from django.db import models
from .role import Roles


class Claims(models.Model):
    id = models.UUIDField(primary_key=True)
    role = models.ForeignKey(Roles, models.DO_NOTHING)
    type = models.TextField()
    value = models.TextField(blank=True, null=True)
