from django.test import TestCase
from users.forms import UserRegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterFormTest(TestCase):

    def test_register_form_renders_fields(self):
        form = UserRegisterForm()

    def test_register_form_validates_mandatory_fields(self):
        form = UserRegisterForm(data={'email': 'testing@random.com',
                                      'password1': 'testingpassword101', 'password2': 'testingpassword101'})
        form.username = form['email']
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(len(User.objects.all()), 1)

        form = UserRegisterForm(data={'email': '', 'password1': '', 'password2': ''})
        self.assertFalse(form.is_valid())

        form = UserRegisterForm(data={'email': 'thisisnotanemail',
                                      'password1': 'testingpassword101', 'password2': 'testingpassword101'})
        self.assertFalse(form.is_valid())

        form = UserRegisterForm(data={'email': 'testing@random.com',
                                      'password1': 'testingpassword101', 'password2': 'testingpassword102'})
        self.assertFalse(form.is_valid())





