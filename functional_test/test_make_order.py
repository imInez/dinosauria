# from base import FunctionalTest
# from helpers import tests_helpers
#
# class NewOrderTest(FunctionalTest):
#
#     def AddItemsToCartTest(self):
#         self.browser.get(self.live_server_url  + '/products/')
#         self.assertEqual(self.browser.current_url, 'http://localhost:8000/products/')
#
#         product_elements = self.browser.find_elements_by_id('product')
#         for el in product_elements:
#             if 'Test' not in el.find_element_by_class_name('product-name').text:
#                 el.click()
#                 self.browser.find_element_by_id('add-to-cart').click()
#
#
#     def LoggedInUserCanMakeOrderTest(self):
#         # Users is logged in and have items in cart, they go to cart page, they have address saved
#         tests_helpers.create_test_user()
#         tests_helpers.login_user()
#         tests_helpers.create_test_items()
#         tests_helpers.add_items_to_cart()
#         tests_helpers.go_to_cart()
#         # They click on make an order and new order is saved to db
#         tests_helpers.make_a_successful_order()
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
#     def GuestUserCanMakeOrderTest(self):
#     #     # User is not logged in, they have items in cart, they go to cart page and click on Order as a guest
#     #     self._create_test_items()
#     #     self._add_items_to_cart()
#     #     self._go_to_cart()
#     #
#     #     # They correctly fill up the shipment form
#     #     # TODO how to find input box?
#     #
#     #     # They are forwarded to order summary page
#     #     # TODO add order id to header
#     #     self.assertIn('Your order: ', self.browser.find_element_by_tag_name('h2').text)
#         pass
#
#     def ForwardToPaymentTest(self):
#         # User wants to make an order, and clicks on Make an order button
#         # They are forwarded to payment gateway
#
#         # All data there is correct
#         pass
#
#     def OrderPaymentConfirmationTest(self):
#         # User clicked on make an order and were forwarded to payment gateway
#         # the payemnt was sucsessful and they were forwarded back to dinosauria
#         # they see order confirmation page
#         pass
#
#     def OrderPaymentFailureTest(self):
#         # User clicked on make an order and were forwarded to payment gateway
#         # the payemnt was not sucsessful and they were forwarded back to dinosauria
#         # they see order failure page
#         pass
#
#     def OrderEmailTest(self):
#         # User makes an order, pays and is forwarded to order confirmation page
#         # the order confirmation mail is sent to user email address
#         pass