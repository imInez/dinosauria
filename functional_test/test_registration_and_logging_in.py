from base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class RegistationAndLoggingInTest(FunctionalTest):

    def test_registration(self):
        # User wants to become a part of Dinosauria land and go to registration page
        self.browser.get(self.live_server_url+'/register/')

        # They provide necessary data
        email_input = self.browser.find_element_by_name('email')
        email_input.send_keys('testing@random.com')
        email_input.send_keys(Keys.ENTER)

        pass_input = self.browser.find_element_by_name('passwrd')
        email_input.send_keys('testingPassword101')
        email_input.send_keys(Keys.ENTER)

        # They click on register button
        register_btn = self.browser.find_element_by_tag_name('button')
        register_btn.send_keys(Keys.ENTER)
        # They are now logged in and redirected to where they came from
        # TODO

    def test_login(self):
        self.browser.get(self.live_server_url + '/login/')
        # TODO story

        # They provide necessary data
        email_input = self.browser.find_element_by_name('email')
        email_input.send_keys('testing@random.com')
        email_input.send_keys(Keys.ENTER)

        pass_input = self.browser.find_element_by_name('passwrd')
        email_input.send_keys('testingPassword101')
        email_input.send_keys(Keys.ENTER)