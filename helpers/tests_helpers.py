from shop.models import Product



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


def create_test_user(self):
    pass


def login_user(self):
    pass


def go_to_cart(self):
    self.browser.get(self.browser.current_url + '/cart/')


def make_a_successful_order(self):
    pass


def make_a_failure_order(self):
    pass
