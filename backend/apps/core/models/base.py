import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase


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


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    # tag = models.ForeignKey(Tag, related_name="uuid_tagged_items", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
