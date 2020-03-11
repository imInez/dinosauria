# from base import FunctionalTest
#
#
# class NewOrderTest(FunctionalTest):
#
#
#     def test_logged_in_user_can_make_an_order(self):
#         # Users is logged in and have items in cart, they go to cart page, they have address saved
#         self._create_test_user()
#         self._login_user()
#         self._create_test_items()
#         self._add_items_to_cart()
#         self._go_to_cart()
#         # They click on make an order and new order is saved to db
#         self.__make_a_successful_order()
#
#         # They are forwarded to order summary page
#         self.assertIn('Your order: ', self.browser.find_element_by_tag_name('h2').text)
#         # They can see their order in their profile
#         self.browser.find_element_by_name('profile').click()
#
#         self.assertIn('Your orders', self.browser.find_element_by_tag_name('h1').text)
#
#         # TODO get order info to check if visible
#
#
#     def test_guest_user_can_make_an_order(self):
#         # User is not logged in, they have items in cart, they go to cart page and click on Order as a guest
#         self._create_test_items()
#         self._add_items_to_cart()
#         self._go_to_cart()
#
#         # They correctly fill up the shipment form
#         # TODO how to find input box?
#
#         # They are forwarded to order summary page
#         # TODO add order id to header
#         self.assertIn('Your order: ', self.browser.find_element_by_tag_name('h2').text)
#
#         pass
#
#     def test_user_is_forwarder_to_payment(self):
#         # User wants to make an order, and clicks on Make an order button
#         # They are forwarded to payment gateway
#
#         # All data there is correct
#         pass
#
#     def test_return_order_confirmation_page_when_payment_successful(self):
#         # User clicked on make an order and were forwarded to payment gateway
#         # the payemnt was sucsessful and they were forwarded back to dinosauria
#         # they see order confirmation page
#         pass
#
#     def test_return_order_failure_page_when_payment_unsuccessful(self):
#         # User clicked on make an order and were forwarded to payment gateway
#         # the payemnt was not sucsessful and they were forwarded back to dinosauria
#         # they see order failure page
#         pass
#
#     def test_send_order_email_confirmation(self):
#         # User makes an order, pays and is forwarded to order confirmation page
#         # the order confirmation mail is sent to user email address
#         pass