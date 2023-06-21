from django.contrib.auth.models import User
from django.test import TestCase


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testuser", password="testpassword")

    def test_user(self):
        # Smoke test
        user = User.objects.get(username="testuser")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.password, "testpassword")
