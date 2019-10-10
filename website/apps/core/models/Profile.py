from django.db import models
from django.contrib.auth.models import User
STATUS_CHOICES = (
    ("Not Approved", 'not_approved'),
    ("Approved", 'approved'),
    ('Banned', 'banned'),
    ('Suspended', 'suspended'),
    ('On_Hollyday', 'on_hollyday')
                  )


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.DO_NOTHING,
                                blank=False,
                                )
    id = models.UUIDField(primary_key=True)
    name = models.TextField()
    nick = models.TextField(unique=True)
    email = models.TextField(unique=True)
    avatar = models.TextField(blank=True, null=True)
    status = models.TextField(choices=STATUS_CHOICES)
    last_login = models.DateTimeField(blank=True, null=True)
    register_date = models.DateTimeField()
    reputation = models.IntegerField(blank=True, null=True)
    impact = models.IntegerField(blank=True, null=True)
    badges = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ('-pk',)
