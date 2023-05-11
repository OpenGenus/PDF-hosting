from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ("first_name", "last_name")
    USERNAME_FIELD = "email"

    objects = UserManager()
