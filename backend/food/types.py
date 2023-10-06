import strawberry_django
from strawberry import auto
from strawberry.relay import Node

from . import models


@strawberry_django.type(models.Item)
class Item(Node):
    amount: auto
    unit: auto
    ingredient: "Ingredient"


@strawberry_django.input(models.Item)
class ItemInput:
    amount: auto
    unit: auto
    ingredient: auto


@strawberry_django.type(models.Ingredient)
class Ingredient(Node):
    name: auto
    inventories: auto
    recipes: auto


@strawberry_django.input(models.Ingredient)
class IngredientInput:
    id: int
    name: auto


@strawberry_django.type(models.Recipe)
class Recipe(Node):
    name: auto
    author: auto
    liked_by: auto
    steps: auto
    photo: auto
    portions: auto


@strawberry_django.input(models.Recipe)
class RecipeInput:
    name: auto
    author: auto
    liked_by: auto
    steps: auto
    photo: auto
    portions: auto
