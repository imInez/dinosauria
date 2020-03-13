from shop.models import Product
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()


def create_test_user(user_model, create_one=True):
    new_user1 = user_model(email='testing1@random.com', password='testingPassword010', username='testing1@random.com')
    # new_user1.username = new_user1.email
    new_user1.save()

    if not create_one:
        new_user2 = user_model(email='testing@2random.com', password='testingPassword010')
        new_user2.username = new_user2.email
        new_user2.save()

        new_user3 = user_model(email='testing@3random.com', password='testingPassword010')
        new_user3.username = new_user3.email
        new_user3.save()
    return user_model.objects.all()


def login_user(self, user, request):
    usr = create_test_user(User).first()
    authenticate(request, usr)


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
    self.browser.get(f'{self.browser.current_url}/products/')

    product_elements = self.browser.find_elements_by_id('product')
    for el in product_elements:
        el.click()
        self.browser.find_element_by_id('add-to-cart').click()


def go_to_cart(self):
    self.browser.get(self.browser.current_url + '/cart/')


def make_a_successful_order(self):
    pass


def make_a_failure_order(self):
    pass
