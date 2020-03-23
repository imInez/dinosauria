from .base import FunctionalTest
from helpers import tests_helpers


class AddProductToBasketTest(FunctionalTest):

    def test_can_add_product_to_basket_from_detail_page(self):
        # User got interested in specific product and visits it's details page
        tests_helpers.create_test_items()
        self.browser.get(self.live_server_url+'/products/')
        chosen_product_link = self.browser.find_element_by_class_name('product-link').get_attribute('href')
        self.browser.get(chosen_product_link)
        # They recognized they love the dinosaur they're viewing and want to buy it, they click on add to basket button
        self.browser.find_element_by_class_name('add-to-cart-btn').click()
        # The product is added to basket
        self.assertEqual(self.browser.find_element_by_tag_name('h3').text, 'Your cart: 1')
        product_names = self.browser.find_element_by_class_name('product-name')
        self.assertIn('Test Dino 1', product_names.text)


    def test_can_add_product_to_basket_from_list_page(self):

        # User is viewing all products page and liked one dinousaur so much they didnt need to go and check the details
        tests_helpers.create_test_items()
        self.browser.get(self.live_server_url + '/products/')
        #TODO they click on a product image and see available options

        # they clink on add to basket button and product is added to the basket
        self.browser.find_element_by_class_name('add-to-cart-btn').click()

        #TODO cart items quantity is updated in navbar
        self.assertEqual(self.browser.find_element_by_tag_name('h3').text, 'Your cart: 1')
        product_names = self.browser.find_element_by_class_name('product-name')
        self.assertIn('Test Dino 1', product_names.text)


    def test_can_update_product_quantity_in_basket(self):
        # User is in a basket and wants to buy more than one piece of product
        tests_helpers.add_items_to_cart_ft(self)

        # they click on plus button and 1 is added to this product quantity
        self.browser.find_element_by_class_name('product-plus').click()
        self.assertEqual(self.browser.find_element_by_tag_name('h3').text, 'Your cart: 2')

        # they click minus and 1 is subtracted form this product quantity
        self.browser.find_element_by_class_name('product-minus').click()
        self.assertEqual(self.browser.find_element_by_tag_name('h3').text, 'Your cart: 1')


    def test_price_changes_on_quantity_update(self):
        # User is in a basket and wants to buy more than one piece of product
        tests_helpers.add_items_to_cart_ft(self)

        # they click on plus button and 1 is added to this product quantity
        price_before = self.browser.find_element_by_class_name('product-total-price').text
        self.browser.find_element_by_class_name('product-plus').click()

        # the price for a product is updated accordingly
        price_after = self.browser.find_element_by_class_name('product-total-price').text
        self.assertEqual(str(2*float(price_before)), str(float(price_after)))

        # they click minus and 1 is subtracted form this product quantity
        self.browser.find_element_by_class_name('product-minus').click()

        # the price for a product is updated accordingly
        price_last = self.browser.find_element_by_class_name('product-total-price').text
        self.assertEqual(price_before, price_last)


    def test_total_price_is_udpated(self):
        # User adds a product to basket
        tests_helpers.add_items_to_cart_ft(self)
        # They can see the total price of the cart equals price of added item
        self.assertEqual(self.browser.find_element_by_tag_name('h3').text, 'Your cart: 1')
        total_cart_before = self.browser.find_element_by_id('total-cart')
        # They decide to add another product to cart
        self.browser.get(self.live_server_url + '/products/')
        self.browser.find_elements_by_class_name('add-to-cart-btn')[1].click()
        # In cart, they now see they have two items
        self.assertEqual(self.browser.find_element_by_tag_name('h3').text, 'Your cart: 2')
        total_cart_after = self.browser.find_element_by_id('total-cart')

        # The total price of cart has now changed
        self.assertNotEqual(total_cart_before, total_cart_after)


#     def test_navbar_qunantity_updates(self):
#         # cart items quantity is updated in navbar
#         self.assertEqual(1, self.browser.find_element_by_id('cart-items').text)