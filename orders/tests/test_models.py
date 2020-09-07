from django.test import TestCase
from orders.models import Order
from helpers import tests_helpers


class ProductModelTest(TestCase):

    def making_an_order(self):
        tests_helpers.create_test_items()
        tests_helpers.make_a_successful_order()
        self.assertEqual(len(Order.objects.all()), 1)


