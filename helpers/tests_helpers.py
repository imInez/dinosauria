from shop.models import Product
from orders.models import Order, OrderProduct
from django.contrib.auth import get_user_model
from users.models import Profile, ShipmentAddress
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from django.utils import timezone

User = get_user_model()
TEST_USER_PASSWORD = 'testingPassword010'
STAGING_SERVER = 'http://' + 'localhost:8000'


def create_test_user(fill_address=False, create_one=True):
    User.objects.all().delete()
    new_user1 = User.objects.create_user(username='testing1@random.com', email='testing1@random.com')
    new_user1.set_password(TEST_USER_PASSWORD)
    new_user1.save()
    new_user1_profile = Profile()
    new_user1_profile.user = new_user1
    new_user1_profile.email = 'testing1@random.com'
    new_user1_profile.phone = '100100100'
    new_user1_profile.save()
    if fill_address:
        create_address(new_user1)

    if not create_one:
        new_user2 = User.objects.create_user(username='testing2@random.com',email='testing@2random.com')
        new_user2.set_password(TEST_USER_PASSWORD)
        new_user2.save()
        new_user2_profile = Profile()
        new_user2_profile.email = 'testing2@random.com'
        new_user1_profile.phone = '200200200'
        new_user2_profile.save()
        if fill_address:
            create_address(new_user2)

        new_user3 = User.objects.create_user(username='testing3@random.com', email='testing@3random.com')
        new_user3.set_password(TEST_USER_PASSWORD)
        new_user3.save()
        new_user3_profile = Profile()
        new_user3_profile.email = 'testing3@random.com'
        new_user1_profile.phone = '300300300'
        new_user3_profile.save()
        if fill_address:
            create_address(new_user2)

    return User.objects.all()


def create_address(user):
    address = ShipmentAddress()
    address.profile = user.profile

    address.name = f'TestName {user.username}'
    address.surname = 'TestSurname'
    address.street = 'TestStreet'
    address.building_flat = '10'
    address.city = 'Test City'
    address.zipcode = '100100'
    address.is_main = True
    address.save()
    return address


def create_user_ft(ft):
    # They click on register link in navbar
    register_link = ft.browser.find_element_by_link_text('register').get_attribute('href')
    ft.browser.get(register_link)

    # They provide necessary data
    email_input = ft.browser.find_element_by_name('email')
    email_input.send_keys('testing@random.com')
    email_input.send_keys(Keys.ENTER)

    pass1_input = ft.browser.find_element_by_name('password1')
    pass1_input.send_keys('testingPassword101')
    pass1_input.send_keys(Keys.ENTER)

    pass2_input = ft.browser.find_element_by_name('password2')
    pass2_input.send_keys('testingPassword101')
    pass2_input.send_keys(Keys.ENTER)


def fill_in_registration_form_ft(ft):
    # They click on register link in navbar
    register_link = ft.browser.find_element_by_link_text('register').get_attribute('href')
    ft.browser.get(register_link)

    # They provide necessary data
    email_input = ft.browser.find_element_by_name('email')
    email_input.send_keys('testing@random.com')
    email_input.send_keys(Keys.ENTER)

    pass1_input = ft.browser.find_element_by_name('password1')
    pass1_input.send_keys('testingPassword101')
    pass1_input.send_keys(Keys.ENTER)

    pass2_input = ft.browser.find_element_by_name('password2')
    pass2_input.send_keys('testingPassword101')


def login_user(client, user=None, fill_address=False):
    if not user:
        user = create_test_user(fill_address=fill_address).first()
    client.login(username=user.email, password=TEST_USER_PASSWORD)


def login_user_ft(ft, usr=None, fill_address=False):
    if not usr:
        usr = create_test_user(fill_address=fill_address).first()
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


def update_user_data_ft(ft, is_user, update_phone=False, update_email=False, update_address=False):
    if is_user:
        email = ''
    else:
        email = 'test@email.com'

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


def update_user_data(email=False, phone=False):
    pass


def _slugify(name):
    return name.replace(' ', '-')


def create_test_items(create_one=False):
    new_prod1 = Product(name='Test Dino 1', price=100, available=True)
    new_prod1.save()

    if not create_one:
        new_prod2 = Product(name='Test Dino 2', price=200, available=True)
        new_prod2.save()

        new_prod3 = Product(name='Test Dino 3', price=300, available=True)
        new_prod3.save()

    for prod in Product.objects.all():
        if not prod.slug:
            prod.slug = _slugify(prod.name)
            prod.save()

    return Product.objects.all()


def add_items_to_cart(cart, products):
    for product in products:
        cart.add_product_to_cart(product)
        cart.save()
    return cart


def add_items_to_cart_ft(ft):
    products = create_test_items()
    ft.browser.get(ft.live_server_url + '/products/')
    ft.browser.find_elements_by_class_name('add-to-cart-btn')[0].click()
    ft.assertEqual(ft.browser.find_element_by_tag_name('h3').text, 'You have 1 item in your cart')


def make_a_successful_order(user, product):
    new_order_product = OrderProduct(product=product, price=product.price, quantity=1)
    new_order_product.save()
    new_order = Order(author=user.profile, address=ShipmentAddress.objects.get(profile=user.profile),
                      created=timezone.now(), last_update=timezone.now(), total=product.price)
    new_order.save()
    new_order.products.add(new_order_product)

    return new_order


def make_a_failure_order(self):
    pass


def fill_in_card_details(ft, success=None):
    number = ft.browser.find_element_by_id('credit-card-number')
    number.send_keys('4111111111111111')
    number.send_keys(Keys.ENTER)
    cvv = ft.browser.find_element_by_id('cvv')
    cvv.send_keys('123')
    cvv.send_keys(Keys.ENTER)
    expiration = ft.browser.find_element_by_id('expiration')
    if success:
        expiration.send_keys('1222')
        expiration.send_keys(Keys.ENTER)
    else:
        expiration.send_keys('0120')
        expiration.send_keys(Keys.ENTER)