from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Inventory(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
