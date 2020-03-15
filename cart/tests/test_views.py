from django.test import TestCase
from django.urls import resolve
from cart.views import cart_checkout
from helpers import tests_helpers
from shop.models import Product
from cart.cart import Cart
from django.test import Client

class CartTest(TestCase):

    factory = Client()
    # cart = Cart(factory)

    def test_cart_url_resolves_to_cart_view(self):
        found = resolve('/cart/')
        self.assertEqual(found.func, cart_checkout)

    def test_cart_view_resolves_to_cart_template(self):
        response = self.client.get('/cart/')
        self.assertTemplateUsed('cart/cart')

    def test_can_add_items_to_cart(self):
        cart = Cart(self.client)
        products = tests_helpers.create_test_items()
        tests_helpers.add_items_to_cart(cart, products)
        self.assertEqual(len(cart), len(products))

    def test_cart_contains_all_added_products(self):
        cart = Cart(self.client)
        products = tests_helpers.create_test_items()
        tests_helpers.create_test_items()
        tests_helpers.add_items_to_cart(cart, products)

        self.assertEqual(len(cart), 6)


        response = self.client.get('/cart/')

        self.assertContains(response, 'Test Dino 1')
        self.assertContains(response, 'Test Dino 2')
        self.assertContains(response, 'Test Dino 3')

    # def test_can_choose_order_method(self):
    #     tests_helpers.create_test_items()
    #     tests_helpers.add_items_to_cart()
    #     response = tests_helpers.go_to_cart()
    #
    #     self.assertContains(response, 'Order as a guest')
    #     self.assertContains(response, 'Register or login')
    #
    # def test_if_logged_can_order(self):
    #     tests_helpers.create_test_user()
    #     tests_helpers.login_user()
    #     tests_helpers.create_test_items()
    #     tests_helpers.add_items_to_cart()
    #     response = tests_helpers.go_to_cart()
    #
    #     self.assertContains(response, 'Buy')
    #
    # def test_request_address_if_missing(self):
    #     pass