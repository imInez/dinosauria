from shop.models import Product
from django.contrib.auth import get_user_model
from users.models import Profile, ShipmentAddress
from django.contrib.auth import authenticate
import os, time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

User = get_user_model()
TEST_USER_PASSWORD = 'testingPassword010'
STAGING_SERVER = 'http://' + 'localhost:8000'


def create_test_user(user_model, create_one=True):
    user_model.objects.all().delete()
    new_user1 = user_model.objects.create_user(username='testing1@random.com', email='testing1@random.com',
                                               password=TEST_USER_PASSWORD)
    new_user1_profile = Profile()
    new_user1_profile.user = new_user1
    new_user1_profile.email = 'testing1@random.com'
    new_user1_profile.save()
    address = ShipmentAddress()
    address.profile = new_user1_profile
    address.save()

    if not create_one:
        new_user2 = user_model.objects.create_user(username='testing2@random.com',email='testing@2random.com',
                                                   password=TEST_USER_PASSWORD)
        new_user2_profile = Profile()
        new_user2_profile.email = 'testing2@random.com'
        new_user2_profile.save()

        new_user3 = user_model.objects.create_user(username='testing3@random.com', email='testing@3random.com',
                                                   password=TEST_USER_PASSWORD)
        new_user3_profile = Profile()
        new_user3_profile.email = 'testing3@random.com'
        new_user3_profile.save()

    return user_model.objects.all()


def login_user(user, client):
    usr = create_test_user(User).first()
    client.login(username=usr.email, password=usr.password)


def login_user_ft(ft):
    usr = create_test_user(User).first()
    ft.browser.get(ft.live_server_url)

    login = ft.browser.find_element_by_link_text('login').get_attribute('href')
    ft.browser.get(login)
    ft.assertIn('Login', ft.browser.title)

    email_input = ft.browser.find_element_by_name('username')
    email_input.send_keys(usr.email)
    email_input.send_keys(Keys.ENTER)

    pass_input = ft.browser.find_element_by_name('password')
    pass_input.send_keys(TEST_USER_PASSWORD)
    pass_input.send_keys(Keys.ENTER)

    ft.wait_for(lambda: ft.browser.find_element_by_id('login-btn').click())


def fill_shipment_form(ft, is_user):
    if is_user:
        email = ''
    else:
        email = 'tets@email.com'

    try:
        fields = {
            'str': ['id_name', 'id_surname','id_street','id_building_flat','id_city','id_zipcode'],
            'email': 'id_email',
            'int': 'id_phone',
        }

        for key, value in fields.items():
            if isinstance(value, list):
                for item in value:
                    field = ft.browser.find_element_by_id(item)
                    if field.text == '':
                        field.send_keys('test input')
                        field.send_keys(Keys.ENTER)
            else:
                field = ft.browser.find_element_by_id(value)
                if field.text == '':
                    if key == 'email':
                        field.send_keys(email)
                        field.send_keys(Keys.ENTER)
                    if key == 'int':
                        field.send_keys('100100100')
                        field.send_keys(Keys.ENTER)
    except StaleElementReferenceException:
        pass
    except NoSuchElementException:
        pass


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


def add_items_to_cart(cart, products):
    for product in products:
        cart.add_product(product)
        cart.save()
    return cart


def add_items_to_cart_ft(ft):
    products = create_test_items()
    ft.browser.get(ft.live_server_url + '/products/')
    ft.browser.find_elements_by_class_name('add-to-cart-btn')[0].click()
    ft.assertEqual(ft.browser.find_element_by_tag_name('h3').text, 'Your cart: 1')


def make_a_successful_order(self):
    pass


def make_a_failure_order(self):
    pass
