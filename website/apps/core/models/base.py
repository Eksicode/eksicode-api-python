import uuid

from django.db import models
from simple_history.models import HistoricalRecords


class Base(models.Model):
    # It is OK for every item inside the db to have a uuid4 id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Some basic statistical and meta values are also OK for every item
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    # This is to keep a history of everything
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
