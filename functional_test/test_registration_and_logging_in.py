from base import FunctionalTest

class RegistationAndLoggingInTest(FunctionalTest):

    def new_user_can_register(self):

        # Anonymous user visits dinosauria store

        # They click on register in navbar

        # They provide the needed data - email and password

        # They click register and new user is created

        pass

    def user_logged_after_registration(self):
        # Anonymous user visits dinosauria store

        # They click on register in navbar

        # They provide the needed data - email and password

        # They click register and new user is created

        # User in now logged

        # User is forwarded to home page

        pass

    def existing_user_can_log_in(self):
        # User exists in a db

        # They click on login link ib navbar to login

        # They provide correct data and are moved back to were they came from
        pass

class UserAuthentication(FunctionalTest):

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