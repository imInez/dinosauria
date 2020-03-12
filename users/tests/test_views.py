from django.test import TestCase
from users.forms import UserRegisterForm
from django.contrib.auth import get_user_model
from users import views
from django.urls import resolve
from django.contrib.auth import authenticate, get_user

User = get_user_model()

class RegistrationTest(TestCase):

    def test_register_url_resolves_register_view(self):
        found = resolve('/users/register/')
        self.assertEqual(found.func, views.register)

    def test_register_view_uses_register_template(self):
        response = self.client.get('/users/register/')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_register_view_POST_request_creates_user(self):
        form = UserRegisterForm(data={'email': 'testing@random.com',
                                      'password1': 'testingpassword101', 'password2': 'testingpassword101'})
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(len(User.objects.all()), 1)

    def test_register_POST_loggs_in(self):
        self.client.post('/users/register/', data={'email': 'testing@random.com',
                                                              'password1': 'testingpassword101',
                                                              'password2': 'testingpassword101',
                                                              'next': '/products/'})
        self.assertTrue(get_user(self.client).is_authenticated)
        self.assertEqual(get_user(self.client).username, 'testing@random.com')
        self.assertEqual(get_user(self.client).email, 'testing@random.com')


    def test_register_POST_redirects_back(self):
        # self.client.get('/products')
        response = self.client.post('/users/register/', data={'email': 'testing@random.com',
                                                              'password1': 'testingpassword101',
                                                              'password2': 'testingpassword101',
                                                              'next': '/products/'})
        self.assertRedirects(response, '/products/')
