import factory
from factory import faker

from food.constants import Units
from food.models import Ingredient, Item, Recipe


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    ingredient = factory.SubFactory("food.factories.IngredientFactory")
    amount = faker.Faker("pyint")
    unit = factory.Iterator(Units.choices, getter=lambda c: c[0])


class IngredientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ingredient

    name = faker.Faker("word")


class RecipeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Recipe

    name = faker.Faker("word")
    author = factory.SubFactory("account.factories.ProfileFactory")

    steps = faker.Faker("text")
    photo = faker.Faker("image_url")
    portions = faker.Faker("pyint")
    active_time = faker.Faker("time")
    waiting_time = faker.Faker("time")

    @factory.post_generation
    def ingredients(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for ingredient in extracted:
                self.ingredient_set.add(ingredient)
