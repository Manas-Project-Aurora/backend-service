from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


def default_username() -> str:
    return uuid.uuid4().hex


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        default=default_username,
    )
    email = models.EmailField(
        unique=True,
        max_length=255,
    )
    telegram_id = models.BigIntegerField(
        null=True,
        blank=True,
    )
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
