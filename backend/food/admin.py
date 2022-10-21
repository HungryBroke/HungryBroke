from django.contrib import admin

from food.models import Ingredient, Item, Recipe

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Item)
