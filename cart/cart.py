from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart():
    def __init__(self, request):
        """Initialize the cart"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # create an empty cart and save it in session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quanity=1, quantity_update=False):
        """Add chosen product to cart"""
        p_id = str(product.id)
        if p_id not in self.cart:
            self.cart[p_id] = {'quantity': 0}
        if quantity_update:
            self.cart[p_id]['quantity'] = quanity
            # self.cart[p_id]['price'] = product.price
        else:
            self.cart[p_id]['quantity'] += quanity

    def subtract(self, product):
        p_id = str(product.id)
        if p_id in self.cart:
            self.cart[p_id]['quantity'] -= 1

    def remove(self, product):
        if str(product.id) in self.cart:
            del self.cart[product.id]
            self.save()

    def save(self):
        self.session.modified = True

    def __len__(self):
        """Count all items"""
        return sum([item['quantity'] for item in self.cart.values()])

    def get_total_price(self):
        return sum(Decimal(item['quanitity']) * item['price'] for item in self.cart.values())


    # def __iter__(self):
    #     """Iterate over cart products and get them form database"""
    #     products_ids = self.cart.keys()



