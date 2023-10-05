from django.contrib import admin

from food.models import Recipe, Ingredient, Item


class IngredientInline(admin.TabularInline):
    model = Ingredient.recipes.through


class ItemInline(admin.TabularInline):
    model = Item


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]
    exclude = ('liked_by',)


class IngredientAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    exclude = ('inventories', 'recipes',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Item)
