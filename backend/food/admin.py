from django.contrib import admin

from food.models import Ingredient, Item, Recipe


class IngredientInline(admin.TabularInline):
    model = Ingredient.recipes.through


class ItemInline(admin.TabularInline):
    model = Item


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]
    exclude = ("liked_by",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    exclude = (
        "inventories",
        "recipes",
    )


admin.site.register(Item)
