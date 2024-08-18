# tasks/tests.py

from django.test import TestCase
from django.contrib.auth.models import User

class UserTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.assertEqual(user.username, 'testuser')
