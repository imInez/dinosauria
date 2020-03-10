from django.test import TestCase
from .cart import Cart



class CanAddItemToBasketTest(TestCase):
    pass







class BasketTest(TestCase):
    def test_add_to_basket_and_check(self):
        if len(Product.objects.all()) == 0:
            new_product1 = Product()
            new_product1.name = 'Test Product1'
            new_product1.price = 100
            new_product1.save()

