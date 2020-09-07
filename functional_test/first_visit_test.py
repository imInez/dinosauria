# run with python functional_test/first_visit_test.py

from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException
from helpers import tests_helpers


class FirstVisitTest(unittest.TestCase):

    sitename = 'http://dinosauria.herokuapp.com'

    MAX_WAIT = 10

    def setUp(self) -> None:
        self.browser = webdriver.Safari()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_view_homepage_structure(self):

        # User wants to buy georgeous dinosaur, they go to dinosauria online store
        self.browser.get(self.sitename)

        # User notices Dinosauria title
        self.assertIn('Dinosauria store', self.browser.title)

        # User notices Dinosauria logo at the top center of the page
        logo_text = self.browser.find_element_by_class_name('nav-logo')
        self.assertEqual('Dinosauria', logo_text.text.strip())

        # User can see trending products listed in the home page as image, name and price
        trending_img = self.browser.find_element_by_id('dinosaur-img')
        trending_name = self.browser.find_element_by_id('dinosaur-name')
        trending_price = self.browser.find_element_by_id('dinosaur-price')
        self.assertTrue(trending_img)
        self.assertTrue(trending_name)
        self.assertTrue(trending_price)

    def wait_for_product_in_cart(self, product_name):
        start_time = time.time()
        while True:
            try:
                product_table = self.browser.find_element_by_id('products')
                product_rows = product_table.find_elements_by_tag_name('tr')
                self.assertIn(product_name, [row.text for row in product_rows])
            except (AssertionError, WebDriverException) as e:
                if time.time()-start_time > self.MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_view_products_list_and_add_to_cart(self):
        self.browser.get(self.sitename)
        # User can click on 'products' button to see products
        products_link = self.browser.find_element_by_link_text('Products')
        self.browser.get(products_link.get_attribute('href'))
        self.assertIn('Dinosauria store - Products', self.browser.title)
        self.assertTrue(self.browser.find_element_by_id('products-list'))

        items_found = list(self.browser.find_elements_by_class_name('product-link'))
        self.assertTrue(len(items_found)>0, 'There are products visible')

        # User can add to cart products from the list
        product = self.browser.find_element_by_class_name('product')
        product_name = product.find_element_by_class_name('product-name')
        buttons = product.find_elements_by_tag_name('input')
        add_button = self.browser.find_element_by_id('add-to-cart')
        add_button.click()
        #
        # # user is notified that product has been added to the basket
        # notification = self.browser.find_element_by_id('added-to-cart-notification')
        # self.assertTrue(notification)

        # cart items value gets updated
        cart_link = self.browser.find_element_by_id('cart')
        self.browser.get(cart_link.get_attribute('href'))
        self.wait_for_product_in_cart(product_name)

    def test_can_view_product_details(self):
        tests_helpers.create_test_items()
        self.browser.get(self.sitename + '/products/')
        # user clicks on product image/name and is taken to product detail page
        self.browser.find_elements_by_class_name('product-link').click()
        # on product page they see images gallery, price, description and [ADD] button
        self.assertTrue(self.browser.find_element_by_class_name('product-img'))
        self.assertTrue(self.browser.find_element_by_name('product-name'))
        self.assertTrue(self.browser.find_element_by_name('product-price'))
        self.assertTrue(self.browser.find_element_by_name('product-id'))
        self.assertTrue(self.browser.find_element_by_name('product-desc'))
        # user clicks on add button
        self.browser.find_elements_by_class_name('add-to-cart-btn')
        # the product is added to the basket, number of items in a basket is increased by one
        self.assertEqual(1, int(self.browser.find_element_by_id('nav-cart-items').text))

    def test_can_register_and_be_logged_in_automatically(self):
        # user does not have the account yet so they click on register button
        # the registration form shows up with fields: email, password, name, surname, address, phone number
        tests_helpers.fill_in_registration_form_ft()
        # user inputs all the data correctly and click on register button
        self.browser.find_element_by_id('register-btn')
        # user is now registered and automatically logged in
        self.assertTrue(self.browser.find_element_by_tag_name('a').text('logout'))


if __name__ == '__main__':
    unittest.main(warnings='ignore')









