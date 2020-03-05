from django.test import TestCase
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from shop.views import home, products
from .models import Product

class PagesTest(TestCase):
    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_products_url_resolves_to_products_view(self):
        found = resolve('/products')
        self.assertEqual(found.func, products)

class ProductModelTestCase(TestCase):
    def test_saving_and_retrieving_product(self):
        new_product1 = Product()
        new_product1.name = 'Test Product1'
        new_product1.price = 100
        new_product1.save()

        new_product2 = Product()
        new_product2.name = 'Test Product2'
        new_product2.price = 10.99
        new_product2.save()

        new_products = Product.objects.all()
        print(new_products)
        self.assertEqual(new_products.count(), 2)

        self.assertEqual(new_products[0].name, 'Test Product1')
        self.assertEqual(new_products[1].name, 'Test Product2')

class BasketTest(TestCase):
    def test_add_to_basket_and_check(self):
        if len(Product.objects.all()) == 0:
            new_product1 = Product()
            new_product1.name = 'Test Product1'
            new_product1.price = 100
            new_product1.save()



    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home(request)
    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>Dinosauria store</title>', html)
    #     self.assertTrue(html.endswith('</html>'))

