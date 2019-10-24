from django.contrib import admin

from .base import BaseModelAdmin
from ..models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(BaseModelAdmin):
    ...
