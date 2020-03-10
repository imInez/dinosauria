from .base import FunctionalTest


class NewOrderTest(FunctionalTest):

    def test_logged_in_user_can_make_an_order(self):
        pass

    def test_guest_user_can_make_an_order(self):
        pass

    def test_user_is_forwarder_to_payment(self):
        pass

    def test_return_order_made_when_payment_successful(self):
        pass

    def test_returns_order_failure_when_payment_unsuccessful(self):
        pass

    def test_send_order_email_confirmation(self):
        pass