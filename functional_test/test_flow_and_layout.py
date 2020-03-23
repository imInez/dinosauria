from .base import FunctionalTest
from shop.models import Product
from helpers import tests_helpers
from selenium.webdriver.common.keys import Keys
from django.contrib.auth import get_user_model
import time


class HomePageFlow(FunctionalTest):
    """ Shop app FTs """
    def test_can_see_homepage_structure(self):

        # User wants to buy georgeous dinosaur, they go to dinosauria online store
        self.browser.get(self.live_server_url)

        # User notices Dinosauria title
        self.assertIn('Dinosauria store', self.browser.title)

        # User notices Dinosauria logo at the top center of the page
        logo_text = self.browser.find_element_by_id('logo-text')
        self.assertEqual('Dinosauria', logo_text.text)
        logo_img = self.browser.find_element_by_id('logo-img')
        self.assertIn('logo-img.png', logo_img.get_attribute('src'))

        # User can see trending products listed in the home page as image, name and price
        trending_img = self.browser.find_element_by_id('dinosaur-img')
        trending_name = self.browser.find_element_by_id('dinosaur-name')
        trending_price = self.browser.find_element_by_id('dinosaur-price')
        self.assertTrue(trending_img)
        self.assertTrue(trending_name)
        self.assertTrue(trending_price)


class ProductListFlow(FunctionalTest):

    def test_can_see_all_products_list_and_details_links(self):
        # User wants to see all available products and go to All products link
        self.browser.get(self.live_server_url)
        products_link = self.browser.find_element_by_link_text('Products').get_attribute('href')
        self.browser.get(products_link)
        # products_link.click()
        self.wait_for(lambda:
                      self.assertIn(self.browser.find_element_by_tag_name('h3').text, 'All products'))

        # User can see all products as pictures in rows
        all_products = self.browser.find_elements_by_class_name('product-link')
        self.assertEqual(len(Product.objects.all()), len(all_products))

        tests_helpers.create_test_items()
        self.browser.get(products_link)
        all_products = self.browser.find_elements_by_class_name('product-link')
        self.assertEqual(len(Product.objects.all()), len(all_products))

        # TODO this will work with js, for now make mvc
        # User clicks on a picture to see available actions - add to basket or see details
        self.assertTrue(self.browser.find_element_by_class_name('add-to-cart-btn'))
        self.assertTrue(self.browser.find_element_by_class_name('product-img'))

class ProductDetailFlow(FunctionalTest):

    def test_can_see_product_details(self):
        product = tests_helpers.create_test_items(create_one=True).first()
        self.browser.get(f'{self.live_server_url}/products/')

        # User clicks on product image to see aviailable action and clicks  on See details button
        details_link = self.browser.find_element_by_class_name('product-link').get_attribute('href')
        self.browser.get(details_link)

        # product_element.click()
        # details_link = self.browser.find_element_by_link_text('See details').get_attribute('src')

        # User is taken to product detail page
        self.browser.get(details_link)
        product_id = self.browser.find_element_by_name('product-id').text

        self.assertEqual(product_id, str(product.id))

        # on product page they see images gallery, price, description
        imgs = 'product-img'
        price = 'product-price'
        desc = 'product-desc'
        product_info = [imgs, price, desc]

        for i in product_info:
            self.assertIn(i, self.browser.page_source)

        # User can also see add to cart button
        self.assertTrue(self.browser.find_element_by_class_name('add-to-cart-btn'))



class UserAccountFlow(FunctionalTest):
    """ Users app FTs """

# def test_can_see_orders_table_in_account(self):
#     # User logs in
#     usr = self._create_test_user()
#     self._login_user()
#
#     self._make_an_order()
#     # They go to their account page and see a list of their orders
#     self.browser.find_element_by_name('profile').click()
#
#     self.assertIn('Your orders', self.browser.find_element_by_tag_name('h1').text)

        # TODO check if order data is here

    def test_can_see_address_and_account_settings(self):
        # User who already has an account wants to login
        tests_helpers.login_user_ft(self)

        # They go to their account page and see their address
        self.browser.get(self.live_server_url + '/users/profile/')
        self.assertTrue(self.browser.find_element_by_id('user-addresses'))

        # and account settings - email and password change button
        self.assertTrue(self.browser.find_element_by_id('user-settings'))


class CartFlow(FunctionalTest):
    """ Cart app FTs """

    def test_cart_shows_items_added_and_cart_form(self):
        tests_helpers.create_test_items()
        self.browser.get(self.live_server_url + '/products/')
        self.browser.find_element_by_class_name('add-to-cart-btn').click()
        self.browser.get(self.live_server_url + '/products/')

        # User wants to check the items they have in cart, they click on cart in navbar and are taken to cart page
        cart_link = self.browser.find_element_by_link_text('cart')
        cart_link.click()
        # time.sleep(2)
        self.browser.get(self.live_server_url + '/cart/')
        self.wait_for(lambda:
                      self.assertIn('Your cart', self.browser.find_element_by_tag_name('h3').text))

        # User sees the items they added to cart - small picture, name, price and quantity
        cart_products = self.browser.find_elements_by_class_name('product-name')
        self.assertEqual(len(cart_products), 1)

        # User sees + and - sign to change quantity of products
        self.assertTrue(self.browser.find_element_by_class_name('product-plus'))
        self.assertTrue(self.browser.find_element_by_class_name('product-minus'))

    def test_cart_empty_when_no_items_added(self):
        # User goes to cart page but didn't add any products to the cart
        response = self.browser.get(self.live_server_url + '/cart/')
        # They see the message saying there's nothing in the cart and encouragement to add products to the cart
        container = self.browser.find_element_by_tag_name('div')
        self.assertTrue(self.browser.find_element_by_id('empty-cart'))

    def test_can_see_login_and_guest_buttons_when_not_logged_in(self):
        # User wants to buy an item, they add it to cart and are forwarded to cart
        tests_helpers.create_test_items()
        self.browser.get(self.live_server_url + '/products/')
        self.browser.find_element_by_class_name('add-to-cart-btn').click()
        self.wait_for(lambda:
                      self.assertTrue(int(self.browser.find_element_by_id('cart-items').text) > 0))

        # They need to chose whether they want to register/login or order as a guest,
        # they see all these options available
        links = self.browser.find_elements_by_tag_name('a')
        self.assertTrue(any(a.get_attribute('href').endswith('#loginform') for a in links))
        self.assertTrue(any(a.get_attribute('href').endswith('#guestform') for a in links))

    def test_user_is_asked_for_address_if_its_missing_from_account_info(self):
        tests_helpers.login_user_ft(self)
        # User is registered and logged in
        # they added item to a cart and were forwarder to cart
        tests_helpers.create_test_items()
        self.browser.get(self.live_server_url + '/products/')
        self.browser.find_element_by_class_name('add-to-cart-btn').click()

        self.wait_for(lambda: self.assertIn('Your cart', self.browser.find_element_by_tag_name('h3').text))
        self.assertTrue(int(self.browser.find_element_by_id('cart-items').text) > 0)

        # it's their first order and they didn't provide shipment info while registering
        # now they need to add the info in cart
        # They see address form where they need to provide their shipment data
        self.wait_for(lambda: self.assertTrue(self.browser.find_element_by_id('userform')))

        tests_helpers.fill_shipment_form(self, is_user=True)
        self.wait_for(lambda: self.browser.find_element_by_id('order-btn'))

    def test_address_form_shows_up_when_order_as_guest_option_was_chosen(self):
        # User has items in a basket and they go to cart page
        tests_helpers.create_test_items()
        self.browser.get(self.live_server_url + '/products/')
        self.browser.find_element_by_class_name('add-to-cart-btn').click()

        self.wait_for(lambda: self.assertIn('Your cart', self.browser.find_element_by_tag_name('h3').text))
        self.assertTrue(int(self.browser.find_element_by_id('cart-items').text) > 0)

        # They want to order as a guest, without registration, and click on Order as a guest button
        guestform = [a for a in self.browser.find_elements_by_tag_name('a')
                     if a.get_attribute('href').endswith('#guestform')][0]
        guestform.click()

        # Shipment address form shows up
        self.wait_for(lambda:self.assertTrue(self.browser.find_element_by_id('guestform')))

        # When shipment address form is correct, the Make order button shows up
        tests_helpers.fill_shipment_form(self, is_user=False)
        self.wait_for(lambda: self.browser.find_element_by_id('update').click())

        self.browser.find_element_by_id('order-btn')

    def test_user_can_make_an_order_immediately_when_logged_in_with_address(self):
        # User registers and fills in shipment data
        self.browser.get(self.live_server_url+'/users/register/')
        register_link = self.browser.find_element_by_link_text('register').get_attribute('href')
        self.browser.get(register_link)
        tests_helpers.fill_shipment_form(self, True)
        email_input = self.browser.find_element_by_name('email')
        email_input.send_keys('testing99@random.com')
        pass1_input = self.browser.find_element_by_name('password1')
        pass1_input.send_keys('testingPassword101')
        pass2_input = self.browser.find_element_by_name('password2')
        pass2_input.send_keys('testingPassword101')
        register_btn = self.browser.find_element_by_id('register-btn')
        self.assertEqual(register_btn.text, 'Register')
        register_btn.click()

        tests_helpers.create_test_items()
        tests_helpers.add_items_to_cart_ft(self)

        # They see the order button
        self.browser.find_element_by_id('order-btn')
