from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import os

MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Safari()
        staging_server = os.environ.get('STAGING SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self) -> None:
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
