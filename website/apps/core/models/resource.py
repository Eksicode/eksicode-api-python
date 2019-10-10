from django.db import models
from django.contrib.auth.models import User
from .tags import Tags


class Resources(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()
    creation_date = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(User, models.DO_NOTHING, db_column='creator', related_name="creator")
    last_edit = models.DateTimeField()
    approved = models.BooleanField()
    appved_user = models.ForeignKey(User, models.DO_NOTHING, db_column='appved_user', related_name="appved_user")


class ResourceComments(models.Model):
    id = models.UUIDField(primary_key=True)
    resource_ud = models.ForeignKey(Resources, models.DO_NOTHING, db_column='resource_ud')
    commenter = models.ForeignKey(User, models.DO_NOTHING, db_column='commenter')
    title = models.TextField()
    comment = models.TextField()


class ResourseTags(models.Model):
    resource = models.ForeignKey(Resources, models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey(Tags, models.DO_NOTHING)
