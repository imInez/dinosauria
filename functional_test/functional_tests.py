from selenium import webdriver
import unittest


class FirstVisitTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Safari()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_view_homepage_structure(self):

        # User wants to buy georgeous dinosaur, they go to dinosauria online store
        self.browser.get('http://localhost:8000')

        # User notices Dinosauria title
        self.assertIn('Dinosauria store', self.browser.title)
        self.fail('Finish the test')

        # User notices Dinosauria logo at the top center of the page

        # User can see the products listed in the home page as image, name and price

        # User can click on 'products' button to see full list of products

    def test_can_view_products_list_and_add_to_cart(self):
        pass
        # User can see all products listed

        # User can add to cart products from the list

        # cart items value gets updated

        # user is notified that producuct has been added to the basket

    def test_can_view_product_details(self):
        pass
        # user clicks on product image/name and is taken to product detail page

        # on product page they see images gallery, price, description and [ADD] button

        # user clicks on add button

        # the product is added to the basket, number of items in a basket is increased by one

        # user is notified that producuct has been added to the basket


    def test_can_add_item_to_basket_and_retrieve_it(self):
        pass

    def test_can_register_and_be_logged_in_automatically(self):
        pass

        # user does not have the account yet so they click on register button

        # the registration form shows up with fields: email, password, name, surname, address, phone number

        # user inputs all the data correctly and click od [JOIN] button

        # user is now registered and automatically logged in


    def test_can_make_order_in_basket_when_registered(self):
        pass
        # user clicks on the basket

        # user can see the products that have been added to the basketm and [buy now] button

        # user click buy now button and is taken to login page

        # user can login or click on button[buy as a guest]

        # user logs in

        # user can now see PAYMENT section where they can choose the way of paying

        # user chooses the way of payment and click on [BUY] button

        # user is taken to the payment gate

        # ** payment is processed and successful

        # user is taken to their Orders site

        # user can see the order they have made and the order number

        # user receives the email confirmation about their order




if __name__ == '__main__':
    unittest.main(warnings='ignore')









