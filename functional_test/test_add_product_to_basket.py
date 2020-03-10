from .base import FunctionalTest

class AddProductToBasketTest(FunctionalTest):

    # user clicks on add button

    # the product is added to the basket, number of items in a basket is increased by one

    # user is notified that producuct has been added to the basket

    def test_can_add_product_to_basket_from_detail_page(self):
        # User got interested in specific product and visits it's details page

        # They recognized they love the dinosaur they're viewing and want to buy it, they click on add to basket button

        # The product is added to basket

        # and the cart items quantity is updated in navbar
        pass

    def test_can_add_product_to_basket_from_list_page(self):
        # User is viewing all products page and liked one dinousaur so much they didnt need to go and check the details
        # they click on a product image and see avaiable options

        # they clink on add to basket button and product is added to the basket,

        # cart items quantity is updated in navbar
        pass

    def test_can_update_product_quantity_in_basket(self):
        # User is in a basket and wants to buy more than one piece of product
        # they click on plus button and 1 is added to this product quantity

        # they click minus and 1 is subtracted form this product quantity

        # eventually, the product quantity equals the primary quantity and all plus buttons click
        pass

    def test_price_changes_on_quantity_update(self):
        # User is in a basket and wants to buy more than one piece of product
        # they click on plus button and 1 is added to this product quantity

        # the price for a product is updated accordingly

        # they click minus and 1 is subtracted form this product quantity
        # the price for a product is updated accordingly

        # The total cart price is updated accordingly
        pass

    def test_cannot_subtract_when_qty_zero_can_delete(self):
        # User has some products in the basket

        # They decided it's too much and want to delete two products from the cart

        # The first product has qty equal 1 and user cannot click on minus button, they clik on X button to delete
        # The product is deleted from the list

        # The product is deleted from cart

        # Total cart price is updated accordingly
        # The second product has qty equal 5, user can click on minus button but clicks on X button to delete it all
        # The product is deleted from the list

        # The product is deleted from cart

        # Total cart price is updated accordingly
        pass

    def test_can_recover_basket_when_closed_browser(self):
        # User has products in their basket, but they need to get back to work and they close the browser window

        # They come back with hope they didn't loose their cart, and the products are still awaiting to be ordered
        pass

    def test_keeps_products_in_basket_after_login_or_registration(self):
        # Not logged user has added some product to the basket and want to make an order

        # They realized they already have an account in dinosauria and login in

        # The products of their choice are still in cart
        pass