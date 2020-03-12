from django.test import TestCase
from shop.models import Product

class ProductModelTest(TestCase):
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
        self.assertEqual(new_products.count(), 2)
        self.assertEqual(new_products[0].name, 'Test Product1')
        self.assertEqual(new_products[1].name, 'Test Product2')