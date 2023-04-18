from django.core.management import BaseCommand

from account.factories import ProfileFactory
from food.factories import IngredientFactory, ItemFactory, RecipeFactory


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Create dummy ingredients, items, and recipes

        profile = self.create_profile("admin", "admin")

        ingredients = [
            self.create_ingredient("Egg"),
            self.create_ingredient("Milk"),
        ]
        items = [
            self.create_item(1, "g", ingredients[0]),
            self.create_item(100, "ml", ingredients[1]),
        ]
        recipe = self.create_recipe(
            name="Omelette",
            author=profile,
            steps="1. Crack the egg into a bowl. 2. Add milk. 3. Mix. 4. Fry.",
            photo="https://www.eatordrink.net/wp-content/uploads/2018/03/vegan-omelette.jpg",
            portions=10,
            ingredients=ingredients,
        )
        # Write created objects to the console
        self.stdout.write(self.style.SUCCESS("Successfully created dummy data"))
        self.stdout.write(self.style.SUCCESS(f"Ingredients: {ingredients}"))
        self.stdout.write(self.style.SUCCESS(f"Items: {items}"))
        self.stdout.write(self.style.SUCCESS(f"Recipe: {recipe}"))
        pass

    def create_item(self, amount: int, unit: str, ingredient) -> ItemFactory:
        return ItemFactory(
            amount=amount,
            unit=unit,
            ingredient=ingredient,
        )

    def create_ingredient(self, name: str) -> IngredientFactory:
        return IngredientFactory(
            name=name,
        )

    def create_recipe(
        self,
        name: str,
        author: ProfileFactory,
        steps: str,
        photo: str,
        portions: int,
        ingredients: list,
    ) -> RecipeFactory:
        return RecipeFactory(
            name=name,
            author=author,
            steps=steps,
            photo=photo,
            portions=portions,
            ingredients=ingredients,
        )

    def create_profile(self, user: str, password) -> ProfileFactory:
        return ProfileFactory(user__username=user, user__password=password, user__is_staff=True)
