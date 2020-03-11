from base import FunctionalTest
from shop.models import Product
import requests
from helpers import tests_helpers

""" Shop app FTs """
class HomePageLayoutStylingTest(FunctionalTest):
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


class ProductListLayoutStylingTest(FunctionalTest):

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

class ProductDetailLayoutStylingTest(FunctionalTest):

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
        self.assertTrue(self.browser.find_element_by_id('add-to-cart'))

""" Cart app FTs """
# class CartLayoutStyling(FunctionalTest):
#
#     def test_cart_shows_items_added_and_cart_form(self):
#         self._create_test_items()
#         self._add_items_to_cart()
#
#         # User wants to check the items they have in cart, they click on cart in navbar and are taken to cart page
#         cart_link = self.browser.find_element_by_id('cart')
#         cart_link.click()
#         self.assertIn('Your cart', self.browser.find_element_by_tag_name('h2').text)
#
#         # User sees the items they added to cart - small picture, name, price and quantity
#         cart_products = self.browser.find_elements_by_partial_link_text('Test Dino')
#         self.assertEqual(len(cart_products), len(Product.objects.all()))
#
#         # User sees + and - sign so change quantity of products
#         self.assertTrue(self.browser.find_element_by_id('cart-add'))
#         self.assertTrue(self.browser.find_element_by_id('cart-subtract'))
#
#     def test_cart_empty_when_no_items_added(self):
#         # User goes to cart page but didn't add any products to the cart
#         self._go_to_cart()
#         # They see the message saying there's nothing in the cart and encouragement to add products to the cart
#         self.assertTrue(self.browse.find_element_by_id('empty-cart'))
#
#     def test_can_see_login_and_guest_buttons_when_not_logged_in(self):
#         # User goes to cart to make an order
#         self._go_to_cart()
#         # They need to chose whether they want to register/login or order as a guest,
#         # they see all these options available
#         self.assertTrue(self.browser.find_element_by_link_text('Login or register').isDisplayed())
#         self.assertTrue(self.browser.find_element_by_link_text('Order as a guest').isDisplayed())
#
#     def test_user_is_asked_for_address_if_its_missing_from_account_info(self):
#         # User is registered and logged in but it's their first order.
#         usr = self._create_test_user()
#         usr.name = ''
#         usr.surname = ''
#         usr.street = ''
#         usr.no_building = ''
#         usr.phone = ''
#         self._login_user()
#         # They have items in a basket and go to cart page
#         self._create_test_items()
#         self._add_items_to_cart()
#         self._go_to_cart()
#         # They see address form where they need to provide their shipment data
#         self.assertTrue(self.browser.find_element_by_id('address-form').isDisplayed())
#         # When the data is provided, the BUY button occurs
#         # TODO how to find input box?
#         name = self.browser.find_element_by_id('address-name')
#         surname = self.browser.find_element_by_id('address-surname')
#         street = self.browser.find_element_by_id('address-street')
#         no_building = self.browser.find_element_by_id('address-building')
#         phone = self.browser.find_element_by_id('address-phone')
#
#     def test_addres_form_shows_up_when_order_as_guest_option_was_chosen(self):
#         # User has items in a basket and they go to cart page
#         self._create_test_items()
#         self._add_items_to_cart()
#         self._go_to_cart()
#
#         self.assertFalse(self.browser.find_element_by_id('address-form').isDisplayed())
#         # They want to order as a guest, without registration, and click on Order as a guest button
#         self.browser.find_element_by_id('guest_button').click()
#         # Shipment addres form shows up
#         self.assertTrue(self.browser.find_element_by_id('address-form').isDisplayed())
#         # When shipment address form is correct, the Make order button shows up
#
#     def test_user_can_make_an_order_immediately_when_logged_in(self):
#         # User logs in
#         usr = self._create_test_user()
#         self._login_user()
#         # They add product to cart and go to cart page
#         self._create_test_items()
#         self._add_items_to_cart()
#         self._go_to_cart()
#         # They see button BUY
#         self.assertTrue(self.browser.find_element_by_id('buy-button').isDisplayed())


""" Users app FTs """
# class UserAccountLayoutStyling(FunctionalTest):
#
#     def test_can_see_orders_table_in_account(self):
#         # User logs in
#         usr = self._create_test_user()
#         self._login_user()
#
#         self._make_an_order()
#         # They go to their account page and see a list of their orders
#         self.browser.find_element_by_name('profile').click()
#
#         self.assertIn('Your orders', self.browser.find_element_by_tag_name('h1').text)
#
#         #TODO check if order data is here
#
#     def test_can_see_address(self):
#         # User logs in
#         usr = self._create_test_user()
#         self._login_user()
#
#         # They go to their account page and see their address and account information - email and password change button
#         self.assertTrue(self.browser.find_element_by_id('addres-form').isDisplayed())
