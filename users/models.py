from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = None
    telegram_id = models.BigIntegerField(
        unique=True,
        db_index=True,
        null=True,
        blank=True,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
