import factory
from django.conf import settings
from factory import faker

from account.models import Inventory, Profile


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    username = faker.Faker("user_name")
    email = faker.Faker("email")


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)


class InventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Inventory

    name = faker.Faker("word")
    user = factory.SubFactory("account.factories.ProfileFactory")
