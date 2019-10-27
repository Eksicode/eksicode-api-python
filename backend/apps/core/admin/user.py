from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .base import BaseModelAdmin
from ..models import User, UserBadge


@admin.register(User)
class UserAdmin(UserAdmin, BaseModelAdmin):
    ...


@admin.register(UserBadge)
class UserBadgeAdmin(BaseModelAdmin):
    ...
