from django.db import models
from taggit.managers import TaggableManager

from .base import Base, UUIDTaggedItem
from ..constants.countries import COUNTRIES
from ..utils.models import Choices


class Vacancy(Base):
    # constants
    countries = Choices(*(country for iso, country in COUNTRIES))

    # title and slug
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)  # Highest theoretical possible value for given title

    # long description
    description = models.TextField()

    # location
    city = models.TextField(blank=True, null=True)
    country = models.CharField(choices=countries.choices, max_length=100)

    # EksiCode personal assignee
    contact_person = models.TextField(blank=True, null=True)

    tags = TaggableManager(through=UUIDTaggedItem)
