from django.test import TestCase
from django.urls import resolve
from cart.views import cart
from helpers import tests_helpers

class CartTest(TestCase):

    def test_cart_url_resolves_to_cart_view(self):
        found = resolve('/cart/')
        self.assertEqual(found.func, cart)

    def test_cart_view_resolves_to_cart_template(self):
        response = self.client.get('/cart/')
        self.assertTemplateUsed('cart/cart')

    def test_cart_contains_all_added_products(self):
        tests_helpers.create_test_items()
        tests_helpers.add_items_to_cart()
        response = tests_helpers.go_to_cart()

        self.assertContains(response, 'Baby Spike')
        self.assertContains(response, 'Blue Rex')
        self.assertContains(response, 'Lollipop T-Rex')

    def test_can_choose_order_method(self):
        tests_helpers.create_test_items()
        tests_helpers.add_items_to_cart()
        response = tests_helpers.go_to_cart()

        self.assertContains(response, 'Order as a guest')
        self.assertContains(response, 'Register or login')

    def test_if_logged_can_order(self):
        tests_helpers.create_test_user()
        tests_helpers.login_user()
        tests_helpers.create_test_items()
        tests_helpers.add_items_to_cart()
        response = tests_helpers.go_to_cart()

        self.assertContains(response, 'Buy')

    def test_request_address_if_missing(self):
        pass