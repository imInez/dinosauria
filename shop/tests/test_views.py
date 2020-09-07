from django.urls import resolve
from django.test import TestCase
from shop.views import home, products, product_details
from helpers import tests_helpers


class HomeTest(TestCase):

    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_root_uses_home_template(self):
        response = self.client.get('')
        self.assertTemplateUsed('shop/home.html')


class ProductListTest(TestCase):

    def test_products_url_resolves_to_products_view(self):
        found = resolve('/products/')
        self.assertEqual(found.func, products)

    def test_products_view_uses_products_tempalate(self):
        response = self.client.get('/products/')
        self.assertTemplateUsed('shop/product/product-list.html')

    def test_products_view_gets_all_product_objects(self):
        products = tests_helpers.create_test_items()
        self.assertEqual(len(products), 3)
        products_names = [product.name for product in products]
        self.assertEqual(products_names, ['Test Dino 1', 'Test Dino 2', 'Test Dino 3'])
        response = self.client.get('/products/')
        for name in products_names:
            self.assertContains(response, name)


class ProductDetailTest(TestCase):

    def test_details_url_resolves_to_detail_view(self):
        product = tests_helpers.create_test_items(create_one=True).first()
        product_link = f'/products/{product.id}/{product.slug}'
        found = resolve(product_link)
        self.assertEqual(found.func, product_details)

    def test_detail_view_uses_detail_template(self):
        product = tests_helpers.create_test_items(create_one=True).first()
        product_link = f'/products/{product.id}/{product.slug}'
        response = self.client.get(product_link)
        self.assertTemplateUsed('shop/product/product-details.html')

    def test_detail_view_shows_correct_product(self):
        products = tests_helpers.create_test_items()
        product_link = f'/products/{products[0].id}/{products[0].slug}'
        response = self.client.get(product_link)
        self.assertContains(response, products[0].name)
        self.assertContains(response, products[0].id)
        self.assertNotContains(response, products[1].name)