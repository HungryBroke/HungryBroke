from django.db import models
from food.constants import Units


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey("account.User", on_delete=models.SET_NULL)
    liked_by = models.ManyToManyField("account.User")

    active_time = models.DurationField()
    waiting_time = models.DurationField()

    steps = models.TextField()
    photo = models.ImageField()
    portions = models.PositiveSmallIntegerField()


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    inventories = models.ManyToManyField("account.Inventory")
    recipes = models.ManyToManyField(Recipe)


class Item(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unit = models.CharField(choices=Units.choices)
