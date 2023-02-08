import strawberry

from food.types import Ingredient, Item, Recipe


@strawberry.type
class Query:
    items: list[Item] = strawberry.django.field()
    ingredients: list[Ingredient] = strawberry.django.field()
    recipes: list[Recipe] = strawberry.django.field()


schema = strawberry.Schema(query=Query)
