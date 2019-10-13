from django.db import models
from taggit.managers import TaggableManager

from .base import Base


class Resource(Base):
    # Name of the resource
    name = models.TextField()

    # Creator of the resource, by creator we mean the person who added it
    creator = models.ForeignKey("User", models.SET_NULL, null=True, blank=True)

    # Status of the Resource
    approved = models.BooleanField()

    # Comments to the resource
    comments = models.ManyToManyField("ResourceComment")

    # tags
    tags = TaggableManager()


class ResourceComment(Base):
    commenter = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
