from datetime import timedelta

import pytest
from django.test import TestCase

from food.factories import IngredientFactory, ItemFactory, RecipeFactory
from food.models import Ingredient, Item, Recipe  # assuming that you have these models
from HungryBroke.schema import schema


class RecipeTestCase(TestCase):
    def setUp(self):
        Recipe.objects.create(
            name="test-recipe",
            active_time=timedelta(minutes=10),
            waiting_time=timedelta(minutes=30),
            portions=2,
        )

    def test_food(self):
        # Smoke test
        recipe = Recipe.objects.get(name="test-recipe")
        self.assertEqual(recipe.name, "test-recipe")


class IngredientTestCase(TestCase):
    def setUp(self):
        Ingredient.objects.create(name="test-ingredient")

    def test_ingredient(self):
        # Smoke test
        ingredient = Ingredient.objects.get(name="test-ingredient")
        self.assertEqual(ingredient.name, "test-ingredient")


class ItemTestCase(TestCase):
    def setUp(self):
        ingredient = Ingredient.objects.create(name="test")
        Item.objects.create(amount=100, ingredient=ingredient)

    def test_item(self):
        # Smoke test
        item = Item.objects.get(amount=100)
        self.assertEqual(item.amount, 100)


class GraphQLTests(TestCase):
    @pytest.mark.django_db
    def test_queries(self):
        # create some objects in the db
        ItemFactory()
        IngredientFactory()
        RecipeFactory()

        # use the client to execute a query
        response = schema.execute_sync(
            """
        {
            items {
                amount
                unit
            }
            ingredients {
                name
            }
            recipes {
                name
            }
        }"""
        )

        # check the response data
        assert response.data["items"][0]["amount"]
        assert response.data["items"][0]["unit"]
        assert response.data["ingredients"][0]["name"]
        assert response.data["recipes"][0]["name"]

    @pytest.mark.django_db
    def test_mutation(self):
        IngredientFactory(id=1)
        response = schema.execute_sync(
            """
        mutation {
            addItem(data: { amount: 100, unit: "g", ingredient:{
                set:"1"
            } }) {
                unit
                amount
            }
        }"""
        )

        # Check the response data
        assert response.data["addItem"]["unit"] == "g"
        assert response.data["addItem"]["amount"] == 100
        # assuming that there are no errors with this mutation

        # Check if it was added to the database
        assert Item.objects.filter(unit="g").exists()
