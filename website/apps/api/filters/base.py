from django_filters import CharFilter, FilterSet
from taggit.forms import TagField


class TagFilter(CharFilter):
    field_class = TagField

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('lookup_expr', 'in')
        super().__init__(*args, **kwargs)

