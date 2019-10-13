from django.contrib import admin

from .base import BaseModelAdmin
from ..models import Resource, ResourceComment


@admin.register(Resource)
class ResourceAdmin(BaseModelAdmin):
    ...

@admin.register(ResourceComment)
class ResourceCommentAdmin(BaseModelAdmin):
    ...
