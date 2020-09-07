from .base import FunctionalTest
from helpers import tests_helpers
import time

class NewOrderTest(FunctionalTest):

    def test_redirects_to_payment_gateway(self):
        tests_helpers.login_user_ft(self, fill_address=True)
        tests_helpers.add_items_to_cart_ft(self)
        # User wants to make an order having items in their cart, and clicks on ORDER button
        self.browser.find_element_by_id('order-btn').click()
        # They are forwarded to payment gateway
        self.assertEqual(self.browser.find_element_by_tag_name('h2').text, 'Pay by credit card')

    ## can't test braintree frame for now
    #
    # def test_redirected_to_successful_order_if_payment_success(self):
    #     # User clicked on make an order and were forwarded to payment gateway
    #     self.test_redirects_to_payment_gateway()
    #     # User provides card details and clicks Pay
    #     print(self.browser.page_source)
    #     tests_helpers.fill_in_card_details(self, success=True)
    #     time.sleep(5)
    #     # the payment was successful and they are forwarded to confirmation page
    #     self.assertEqual(self.browser.find_element_by_tag_name('h3').text, 'Your payment was successful!')
    #
    # def test_not_redirected_if_payment_failed(self):
    #     # User clicked on make an order and were forwarded to payment gateway
    #     self.test_redirects_to_payment_gateway()
    #     # User provides card details and clicks Pay
    #     tests_helpers.fill_in_card_details(self, success=True)
    #     # the expiration date is not correct, so it's highlighted in red and Pay button didn't work
    #     self.assertContains(self.browser.find_element_by_id('expiration').get_attribute('class'), 'invalid')
    #
    # def test_order_status_change_when_payment_processed(self):
    #     self.test_redirected_to_successful_order_if_payment_success()
    #     self.browser.get(self.live_server_url + 'users/profile/')
    #     orders = self.browser.find_element_by_id('user-orders')
    #     for row in orders.find_elements_by_class_name('my-3 py-3'):
    #         for details in row.find_elements_by_class_name('sans-font'):
    #             self.assertContains(details, 'Payment status SUCCESSFUL')
    #
    #
    # def test_new_order_email_sent(self):
    #     # User makes an order, pays and is forwarded to order confirmation page
    #     # the order confirmation mail is sent to user email address
    #     pass
    #
    # def test_email_sent_on_order_status_change(self):
    #     pass
