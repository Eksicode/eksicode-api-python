from django.db import models
from .elements import Countries

class VacancyGroup(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()


class Vacancies(models.Model):
    id = models.UUIDField(primary_key=True)
    vacancy_group = models.ForeignKey(VacancyGroup, models.DO_NOTHING, db_column='vacancy_group')
    title = models.TextField()
    slug = models.TextField()
    description = models.TextField()
    city = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='country')
    contact_person = models.TextField(blank=True, null=True)
