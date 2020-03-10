from .base import FunctionalTest

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
