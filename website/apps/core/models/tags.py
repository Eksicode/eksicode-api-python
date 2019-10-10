from django.db import models


class Tags(models.Model):
    tag = models.TextField(primary_key=True)
    name = models.TextField()