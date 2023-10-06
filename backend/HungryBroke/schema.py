import strawberry
from strawberry_django.mutations import mutations

from food.types import Ingredient, IngredientInput, Item, ItemInput, Recipe, RecipeInput


@strawberry.type
class Query:
    items: list[Item] = strawberry.django.field()
    ingredients: list[Ingredient] = strawberry.django.field()
    recipes: list[Recipe] = strawberry.django.field()


@strawberry.type
class Mutation:
    addItem: Item = mutations.create(ItemInput)
    addIngredient: Ingredient = mutations.create(IngredientInput)
    addRecipe: Recipe = mutations.create(RecipeInput)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
