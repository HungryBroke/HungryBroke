from django.db import models

from account.models import Inventory, Profile
from food.constants import Units


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True
    )
    liked_by = models.ManyToManyField(Profile, related_name="liked_recipes")

    active_time = models.DurationField()
    waiting_time = models.DurationField()

    steps = models.TextField()
    photo = models.ImageField()
    portions = models.PositiveSmallIntegerField()


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    inventories = models.ManyToManyField(Inventory)
    recipes = models.ManyToManyField(Recipe)


class Item(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unit = models.CharField(choices=Units.choices, max_length=3)
