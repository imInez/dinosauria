from django.test import TestCase
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from shop.views import home

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home(request)
    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>Dinosauria store</title>', html)
    #     self.assertTrue(html.endswith('</html>'))

