from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException


class FirstVisitTest(unittest.TestCase):

    MAX_WAIT = 10

    def setUp(self) -> None:
        self.browser = webdriver.Safari()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_view_homepage_structure(self):

        # User wants to buy georgeous dinosaur, they go to dinosauria online store
        self.browser.get('http://localhost:8000')

        # User notices Dinosauria title
        self.assertIn('Dinosauria store', self.browser.title)
        # self.fail('Finish the test')

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
        self.browser.get('http://localhost:8000')
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
        add_button = product.find_element_by_tag_name('button')
        add_button.click()

        # user is notified that product has been added to the basket
        notification = self.browser.find_element_by_id('added-to-cart-notification')
        self.assertTrue(notification)

        # cart items value gets updated
        cart_link = self.browser.find_element_by_id('cart')
        self.browser.get(cart_link.get_attribute('href'))
        self.wait_for_product_in_cart(product_name)


    def test_can_view_product_details(self):
        pass
        # user clicks on product image/name and is taken to product detail page

        # on product page they see images gallery, price, description and [ADD] button

        # user clicks on add button

        # the product is added to the basket, number of items in a basket is increased by one

        # user is notified that producuct has been added to the basket


    def test_can_add_item_to_basket_and_retrieve_it(self):
        pass

    def test_can_register_and_be_logged_in_automatically(self):
        pass

        # user does not have the account yet so they click on register button

        # the registration form shows up with fields: email, password, name, surname, address, phone number

        # user inputs all the data correctly and click od [JOIN] button

        # user is now registered and automatically logged in


    def test_can_make_order_in_basket_when_registered(self):
        pass
        # user clicks on the basket

        # user can see the products that have been added to the basketm and [buy now] button

        # user click buy now button and is taken to login page

        # user can login or click on button[buy as a guest]

        # user logs in

        # user can now see PAYMENT section where they can choose the way of paying

        # user chooses the way of payment and click on [BUY] button

        # user is taken to the payment gate

        # ** payment is processed and successful

        # user is taken to their Orders site

        # user can see the order they have made and the order number

        # user receives the email confirmation about their order




if __name__ == '__main__':
    unittest.main(warnings='ignore')









