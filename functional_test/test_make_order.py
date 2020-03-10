from .base import FunctionalTest


class NewOrderTest(FunctionalTest):

    def _put_items_to_cart(self):
        pass

    def _login_user(self):
        pass

    def _go_to_cart(self):
        pass


    def test_logged_in_user_can_make_an_order(self):
        # Users is logged in and have items in cart, they go to cart page, they have address saved

        # They click on make an order and new order is saved to db with payment=ongoing flag

        pass

    def test_guest_user_can_make_an_order(self):
        # User is not logged in, they have items in cart, they go to cart page and click on Order as a guest

        # They correctly fill up the shipment form

        # They click on Make an order button and one-time user is created ifn db to handle the order,
        # and an order is created in db
        pass

    def test_user_is_forwarder_to_payment(self):
        # User wants to make an order, and clicks on Make an order button
        # They are forwarded to payment gateway

        # All data there is correct
        pass

    def test_return_order_confirmation_page_when_payment_successful(self):
        # User clicked on make an order and were forwarded to payment gateway
        # the payemnt was sucsessful and they were forwarded back to dinosauria
        # they see order confirmation page
        pass

    def test_return_order_failure_page_when_payment_unsuccessful(self):
        # User clicked on make an order and were forwarded to payment gateway
        # the payemnt was not sucsessful and they were forwarded back to dinosauria
        # they see order failure page
        pass

    def test_send_order_email_confirmation(self):
        # User makes an order, pays and is forwarded to order confirmation page
        # the order confirmation mail is sent to user email address
        pass