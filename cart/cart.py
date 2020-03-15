from decimal import Decimal
from django.conf import settings
from shop.models import Product
import time
class Cart(object):
    def __init__(self, request):
        """Initialize the cart"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # create an empty cart and save it in session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, quantity_update=False):
        """Add chosen product to cart"""
        p_id = str(product.id)
        if p_id not in self.cart:
            self.cart[p_id] = {'quantity': 0}
        if quantity_update:
            self.cart[p_id]['quantity'] = quantity
            # self.cart[p_id]['price'] = product.price
        else:
            self.cart[p_id]['quantity'] += quantity
        self.save()

    def add_product(self, product):
        self.cart[product.id] = {'product': product, 'price': product.price,
                                 'quantity': 1, 'total_price': product.price}

    def subtract(self, product):
        p_id = str(product.id)
        if p_id in self.cart:
            self.cart[p_id]['quantity'] -= 1

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['quantity']) * item['price'] for item in self.cart.values())

    def get_all_items(self):
        return self.cart.keys()

    def __len__(self):
        """Count all items"""
        return sum([item['quantity'] for item in self.cart.values()])

    def __iter__(self):
        """Iterate over cart products and get them form database"""
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
            cart[str(product.id)]['price'] = product.price
            cart[str(product.id)]['total_price'] = product.price * cart[str(product.id)]['quantity']


        for item in cart.values():
            yield item











