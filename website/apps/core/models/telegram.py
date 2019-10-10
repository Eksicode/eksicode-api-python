from django.db import models


class TelegramGroups(models.Model):
    name = models.TextField()
    icon = models.TextField()
    user_count = models.IntegerField()
    group_id = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
