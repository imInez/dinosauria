from base import FunctionalTest
from helpers import tests_helpers

class NewOrderTest(FunctionalTest):

    def test_redirects_to_payment_gateway(self):
        # User wants to make an order, and clicks on Make an order button
        # They are forwarded to payment gateway
        # All data there is correct
        pass

    def test_redirected_to_successful_order_if_payment_success(self):
        # User clicked on make an order and were forwarded to payment gateway
        # the payment was successful and they were forwarded back to dinosauria
        # they see order confirmation page
        pass

    def test_redirected_to_failed_order_if_payment_failed(self):
        # User clicked on make an order and were forwarded to payment gateway
        # the payment was not successful and they were forwarded back to dinosauria
        # they see order failure page
        pass

    def test_order_status_change_when_payment_processed(self):
        pass

    def test_new_order_email_sent(self):
        # User makes an order, pays and is forwarded to order confirmation page
        # the order confirmation mail is sent to user email address
        pass

    def test_email_sent_on_order_status_change(self):
        pass
