from django.db import models
from django.contrib.auth.models import User


class Roles(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()


class UserRole(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey(Roles, models.DO_NOTHING)

    class Meta:
        unique_together = (('user', 'role'),)
