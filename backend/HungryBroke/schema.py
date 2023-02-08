from typing import List

import strawberry

from food.types import Item, Ingredient, Recipe


@strawberry.type
class Query:
    items: List[Item] = strawberry.django.field()
    ingredients: List[Ingredient] = strawberry.django.field()
    recipes: List[Recipe] = strawberry.django.field()


schema = strawberry.Schema(query=Query)