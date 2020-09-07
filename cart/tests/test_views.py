from django.test import TestCase
from django.urls import resolve
from cart.views import cart_checkout
from helpers import tests_helpers
from cart.cart import Cart


class CartTest(TestCase):

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
        session = self.client.session
        cart = Cart(request=None, session=session)
        session.save()
        products = tests_helpers.create_test_items()
        tests_helpers.add_items_to_cart(cart=cart, products=products)
        self.assertIsNotNone(session['cart'].keys())
