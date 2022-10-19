from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ...


class Inventory(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)