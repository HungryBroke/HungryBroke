import strawberry
from strawberry import auto

from . import models


@strawberry.django.type(models.Item)
class Item:
    id: auto
    amount: auto
    unit: auto
    ingredient: "Ingredient"


@strawberry.django.type(models.Ingredient)
class Ingredient:
    id: auto
    name: auto
    inventories: auto
    recipes: auto


@strawberry.django.type(models.Recipe)
class Recipe:
    id: auto
    name: auto
    author: auto
    liked_by: auto
    # active_time: auto
    # waiting_time: auto
    steps: auto
    photo: auto
    portions: auto
