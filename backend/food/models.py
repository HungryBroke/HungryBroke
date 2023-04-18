from django.db import models

from account.models import Inventory, Profile
from food.constants import Units


class Recipe(models.Model):
    """
    A recipe is a set of steps to make a dish.
    """

    name = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    liked_by = models.ManyToManyField(Profile, related_name="liked_recipes")

    active_time = models.DurationField(
        help_text="The time the recipe takes to make, excluding waiting time."
    )
    waiting_time = models.DurationField(
        help_text="The time the recipe takes to make, excluding active time."
    )

    steps = models.TextField()
    photo = models.ImageField()
    portions = models.PositiveSmallIntegerField()


class Ingredient(models.Model):
    """
    An ingredient is a type of food.
    """

    name = models.CharField(max_length=255)
    inventories = models.ManyToManyField(Inventory)
    recipes = models.ManyToManyField(Recipe)


class Item(models.Model):
    """
    An item is a specific amount of an ingredient.
    """

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unit = models.CharField(choices=Units.choices, max_length=3)
