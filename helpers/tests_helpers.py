from shop.models import Product
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
import os

User = get_user_model()
TEST_USER_PASSWORD = 'testingPassword010'
STAGING_SERVER = 'http://' + 'localhost:8000'

def create_test_user(user_model, create_one=True):
    new_user1 = user_model.objects.create_user(username='testing1@random.com', email='testing1@random.com',
                                               password=TEST_USER_PASSWORD)

    if not create_one:
        new_user2 = user_model.objects.create_user(username='testing2@random.com',email='testing@2random.com',
                                                   password=TEST_USER_PASSWORD)

        new_user3 = user_model.objects.create_user(username='testing3@random.com', email='testing@3random.com',
                                                   password=TEST_USER_PASSWORD)

    return user_model.objects.all()


def login_user(self, user, client):
    usr = create_test_user(User).first()
    client.login(username=usr.email, password=usr.password)


def _slugify(name):
    return(name.replace(' ', '-'))


def create_test_items(create_one=False):
    new_prod1 = Product(name='Test Dino 1', price=100)
    new_prod1.save()

    if not create_one:
        new_prod2 = Product(name='Test Dino 2', price=200)
        new_prod2.save()

        new_prod3 = Product(name='Test Dino 3', price=300)
        new_prod3.save()

    for prod in Product.objects.all():
        if not prod.slug:
            prod.slug = _slugify(prod.name)
            prod.save()

    return Product.objects.all()


def add_items_to_cart(self):
    self.browser.get(STAGING_SERVER + '/products/')
    self.assertEqual(self.browser.current_url, 'http://localhost:8000/products/')

    product_elements = self.browser.find_elements_by_id('product')
    for el in product_elements:
        if 'Test' not in el.find_element_by_class_name('product-name').text:
            el.click()
            self.browser.find_element_by_id('add-to-cart').click()


def go_to_cart(self):
    return self.browser.get(STAGING_SERVER + '/cart/')


def make_a_successful_order(self):
    pass


def make_a_failure_order(self):
    pass
