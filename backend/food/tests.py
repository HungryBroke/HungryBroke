from django.test import TestCase

from food.models import Ingredient, Item, Recipe

# Create your tests here.


class RecipeTestCase(TestCase):
    def setUp(self):
        Recipe.objects.create(name="test-recipe", description="test-description")

    def test_food(self):
        # Smoke test
        recipe = Recipe.objects.get(name="test-recipe")
        self.assertEqual(recipe.name, "test-recipe")
        self.assertEqual(recipe.description, "test-description")


class IngredientTestCase(TestCase):
    def setUp(self):
        Ingredient.objects.create(name="test-ingredient", description="test-description")

    def test_ingredient(self):
        # Smoke test
        ingredient = Ingredient.objects.get(name="test-ingredient")
        self.assertEqual(ingredient.name, "test-ingredient")
        self.assertEqual(ingredient.description, "test-description")


class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="test-item", description="test-description")

    def test_item(self):
        # Smoke test
        item = Item.objects.get(name="test-item")
        self.assertEqual(item.name, "test-item")
        self.assertEqual(item.description, "test-description")
