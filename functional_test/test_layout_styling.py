from .base import FunctionalTest


class HomePageLayoutStylingTest(FunctionalTest):
    def test_can_see_homepage_structure(self):

        # User wants to buy georgeous dinosaur, they go to dinosauria online store
        self.browser.get('http://localhost:8000')

        # User notices Dinosauria title
        self.assertIn('Dinosauria store', self.browser.title)

        # User notices Dinosauria logo at the top center of the page
        logo_text = self.browser.find_element_by_id('logo-text')
        self.assertEqual('Dinosauria', logo_text.text)
        logo_img = self.browser.find_element_by_id('logo-img')
        self.assertIn('logo-img.png', logo_img.get_attribute('src'))

        # User can see trending products listed in the home page as image, name and price
        trending_img = self.browser.find_element_by_id('dinosaur-img')
        trending_name = self.browser.find_element_by_id('dinosaur-name')
        trending_price = self.browser.find_element_by_id('dinosaur-price')
        self.assertTrue(trending_img)
        self.assertTrue(trending_name)
        self.assertTrue(trending_price)



class ProductListLayoutStylingTest(FunctionalTest):


    def test_can_see_all_products_list_and_details_links(self):
        # User wants to see all available products and go to All products link

        # User can see all products as pictures in rows

        # User clicks on a picture to see available actions - add to basket or see details
        pass


class ProductDetailLayoutStylingTest(FunctionalTest):

    def test_can_see_product_details(self):
        pass
        # User clicks on product image to see aviailable action and then on see details and is taken to product detail page

        # on product page they see images gallery, price, description and cart form



class CartLayoutStyling(FunctionalTest):

    def test_cart_shows_items_added_and_cart_form(self):
        # User wants to check the items thet have in cart, they click on cart in navbar and are taken to cart page

        # User sees the items they added to cart - small picture, name, price and quantity

        # User sees + and - sign so change quantity of products
        pass

    def test_cart_empty_when_no_items_added(self):
        # User goes to cart page but didn't add any products to the cart

        # They see the message saying there's nothing in the cart and encouragement to add products to the cart
        pass

    def test_can_see_login_and_guest_buttons_when_not_logged_in(self):
        # User goes to cart to make an order

        # They need to chose whether they want to register/login or order as a guest,
        # they see all these options available
        pass

    def test_user_can_make_an_order_immediately_when_logged_in(self):
        # User logs in

        # They add product to cart and go to cart page

        # They see button Make an order

        pass



class UserAccountLayoutStyling(FunctionalTest):

    def test_can_see_orders_table_in_account(self):
        # User logs in

        # They go to their account page and see a list of their orders
        pass

    def test_can_see_address(self):
        # User logs in

        # They go to their account page and see their address and account information - email and password change button

        pass