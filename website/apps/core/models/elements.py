from django.db import models


class Menu(models.Model):
    parent = models.IntegerField(blank=True, null=True)
    name = models.TextField()
    slug = models.TextField()


class Countries(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    name = models.TextField()