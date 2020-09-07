from django.test import TestCase
from django.contrib.auth import get_user_model
from helpers.tests_helpers import create_test_user

User = get_user_model()


class UserModelTest(TestCase):

    def test_creating_new_user(self):
        create_test_user()
        self.assertEqual(len(User.objects.all()), 1)
        self.assertEqual(User.objects.first().email, 'testing1@random.com')

    def test_email_uniqueness(self):
        create_test_user(create_one=False)
        self.assertEqual(len(User.objects.all()), 3)
        self.assertNotEqual(User.objects.all()[0].email, User.objects.all()[1].email)

