from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import os
import time
from shop.models import Product

MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Safari()
        staging_server = os.environ.get('STAGING SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self) -> None:
        # Product.objects.all().delete()
        self.browser.quit()


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

    def wait_for(self, f):
        start_time = time.time()
        while True:
            try:
                return f()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    # def get_input_field(self):
    #     return self.browser.find_element_by_id('id_text')

    def _create_test_items(self):
        new_prod1 = Product(name='Test Dino 1', price=100)
        new_prod1.save()

        new_prod2 = Product(name='Test Dino 2', price=200)
        new_prod2.save()

        new_prod3 = Product(name='Test Dino 3', price=300)
        new_prod3.save()

    def _add_items_to_cart(self):
        self.browser.get(f'{self.browser.current_url}/products/')

        product_elements = self.browser.find_elements_by_id('product')
        for el in product_elements:
            el.click()
            self.browser.find_element_by_id('add-to-cart').click()

    def _create_test_user(self):
        pass

    def _login_user(self):
        pass

    def _go_to_cart(self):
        self.browser.get(self.browser.current_url+'/cart/')

    def _make_a_successful_order(self):
        pass

    def _make_a_failure_order(self):
        pass





