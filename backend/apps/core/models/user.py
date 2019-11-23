from django.contrib.auth.models import AbstractUser
from django.db import models

from .base import Base
from ..utils.models import Choices


class User(AbstractUser, Base):
    # Constants
    statuses = Choices(
        "Not Approved",
        "Approved",
        "Banned",
        "Suspended",
        "On Holiday",
    )

    # Profile picture
    avatar = models.ImageField(default='path_to_default_profile_photo')
    # Reputation and impact of the users from answering the questions
    reputation = models.IntegerField(default=0)
    impact = models.IntegerField(default=0)
    # Activeness status of the user
    status = models.TextField(choices=statuses.choices)

    # Badges a user earned
    badges = models.ManyToManyField("UserBadge")

    # Telegram Informations
    telegram_username = models.TextField(max_length=50, unique=True)

class UserBadge(Base):
    name = models.CharField(max_length=100)
    icon = models.ImageField()


def get_default_profile_photo():
    """Function to get an """
    raise
