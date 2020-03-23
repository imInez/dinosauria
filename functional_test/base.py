from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import os
import time
from shop.models import Product
from django.contrib.auth import settings
from importlib import import_module

MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
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

class SessionTestCase(FunctionalTest):

    def get_session(self):
        if self.client.session:
            session = self.client.session
        else:
            session_engine = import_module(settings.SESSION_ENGINE)
            session = session_engine.SessionStore()
        return session

    def set_session_cookies(self, session):
        session_cookie = session.SESSION_COOKIE_NAME
        self.client.cookies[session_cookie] = session.session_key
        cookie_data = {
            'max-age': None,
            'path': '/',
            'domain': settings.SESSION_COOKIE_DOMAIN,
            'secure': settings.SESSION_COOKIE_SECURE or None,
            'expires': None}
        self.client.cookies[session_cookie].update(cookie_data)








