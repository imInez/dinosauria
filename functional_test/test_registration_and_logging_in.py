from base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from django.contrib.auth import get_user_model
from django.test import Client


User = get_user_model()
c = Client()
class RegistrationAndLoggingInTest(FunctionalTest):

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



    def test_registration_stay_loggedin(self):
        # User wants to register to Dinosauria and dont want to have to log in after hat
        self.browser.get(self.live_server_url+'/users/register/')
        register = self.browser.find_element_by_link_text('register')
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

        # pass1_input = self.browser.find_element_by_name('password1')

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




    # def test_login(self):
    #     self.browser.get(self.live_server_url + '/login/')
    #     # TODO story
    #
    #     # They provide necessary data
    #     email_input = self.browser.find_element_by_name('email')
    #     email_input.send_keys('testing@random.com')
    #     email_input.send_keys(Keys.ENTER)
    #
    #     pass_input = self.browser.find_element_by_name('passwrd')
    #     email_input.send_keys('testingPassword101')
    #     email_input.send_keys(Keys.ENTER)