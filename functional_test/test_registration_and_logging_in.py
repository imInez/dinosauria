from base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from django.contrib.auth import get_user_model
from helpers import tests_helpers
import time


User = get_user_model()


class RegistrationTest(FunctionalTest):

    def test_registration_creates_user(self):
        # User wants to become a part of Dinosauria land and go to registration page
        self.browser.get(self.live_server_url+'/users/register/')
        register_link = self.browser.find_element_by_link_text('register').get_attribute('href')
        self.browser.get(register_link)

        # They provide necessary data
        email_input = self.browser.find_element_by_name('email')
        email_input.send_keys('testing99@random.com')
        email_input.send_keys(Keys.ENTER)

        pass1_input = self.browser.find_element_by_name('password1')
        pass1_input.send_keys('testingPassword101')
        pass1_input.send_keys(Keys.ENTER)

        pass2_input = self.browser.find_element_by_name('password2')
        pass2_input.send_keys('testingPassword101')
        pass2_input.send_keys(Keys.ENTER)

        # They click on register button
        register_btn = self.browser.find_element_by_id('register-btn')
        self.assertEqual(register_btn.text, 'Register')
        register_btn.click()

        # They're account is created
        self.assertEqual(len(User.objects.all()), 1)


    def test_registration_redirects_back(self):
        # User wants to register on Dinosauria page and when done they want to get back to the page they came from
        # Now they're on products page
        products_link = self.live_server_url + '/products/'
        self.browser.get(products_link)

        #They click on register link in navbar
        register_link = self.browser.find_element_by_link_text('register').get_attribute('href')
        self.browser.get(register_link)

        # They provide necessary data
        email_input = self.browser.find_element_by_name('email')
        email_input.send_keys('testing@random.com')
        email_input.send_keys(Keys.ENTER)

        pass1_input = self.browser.find_element_by_name('password1')
        pass1_input.send_keys('testingPassword101')
        pass1_input.send_keys(Keys.ENTER)

        pass2_input = self.browser.find_element_by_name('password2')
        pass2_input.send_keys('testingPassword101')
        pass2_input.send_keys(Keys.ENTER)

        # They click on register button
        register_btn = self.browser.find_element_by_id('register-btn')
        self.assertEqual(register_btn.text, 'Register')
        register_btn.click()

        # They are now logged in and redirected to where they came from
        self.assertEqual(self.browser.current_url, products_link)


    def test_registration_stay_logged_in(self):
        # User wants to register to Dinosauria and dont want to have to log in after hat
        self.browser.get(self.live_server_url+'/users/register/')
        register_link = self.browser.find_element_by_link_text('register').get_attribute('href')
        self.browser.get(register_link)

        # They provide necessary data
        email_input = self.browser.find_element_by_name('email')
        email_input.send_keys('testing@random.com')
        email_input.send_keys(Keys.ENTER)

        pass1_input = self.browser.find_element_by_name('password1')
        pass1_input.send_keys('testingPassword101')
        pass1_input.send_keys(Keys.ENTER)

        pass2_input = self.browser.find_element_by_name('password2')
        pass2_input.send_keys('testingPassword101')
        pass2_input.send_keys(Keys.ENTER)

        # They click on register button
        register_btn = self.browser.find_element_by_id('register-btn')
        self.assertEqual(register_btn.text, 'Register')
        register_btn.click()

        # They are now logged in
        try:
            self.browser.find_element_by_link_text('register')
        except NoSuchElementException:
            pass
        else:
            self.fail('register found, user not logged in')

class LoginTest(FunctionalTest):

    def test_existing_user_can_login(self):
        # User who already has an account wants to login
        usr = tests_helpers.create_test_user(User).first()

        # they go to dinosauria home page and click on login btn
        self.browser.get(self.live_server_url)

        login = self.browser.find_element_by_link_text('login').get_attribute('href')
        self.browser.get(login)
        self.assertIn('Login', self.browser.title)

        # They provide necessary data
        email_input = self.browser.find_element_by_name('username')
        email_input.send_keys(usr.email)
        email_input.send_keys(Keys.ENTER)

        pass_input = self.browser.find_element_by_name('password')
        pass_input.send_keys(tests_helpers.TEST_USER_PASSWORD)
        pass_input.send_keys(Keys.ENTER)

        time.sleep(2)
        # They are now logged in
        try:
            self.browser.find_element_by_link_text('register')
        except NoSuchElementException:
            pass
        else:
            self.fail('register found, user not logged in')

    def test_login_redirects_back(self):
        # User is viewing all products and decides to log in, but wants to be taken back to products
        usr = tests_helpers.create_test_user(User).first()
        self.assertEqual(len(User.objects.all()), 1)

        # Now they're on products page
        products_link = self.live_server_url + '/products/'
        self.browser.get(products_link)

        # They click on login link in navbar
        login_link = self.browser.find_element_by_link_text('login').get_attribute('href')
        self.browser.get(login_link)
        self.wait_for(lambda:self.assertEqual(self.browser.current_url,
                                              self.live_server_url + '/users/login/?next=/products/'))

        # They provide necessary data
        email_input = self.browser.find_element_by_name('username')
        email_input.send_keys(usr.username)
        email_input.send_keys(Keys.ENTER)

        pass_input = self.browser.find_element_by_name('password')
        pass_input.send_keys(tests_helpers.TEST_USER_PASSWORD)
        pass_input.send_keys(Keys.ENTER)

        time.sleep(2)
        # They are now logged in and redirected to where they came from
        self.assertEqual(self.browser.current_url, products_link)




