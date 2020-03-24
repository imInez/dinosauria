from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
    def __init__(self, request, session=None):
        """Initialize the cart"""
        if request:
            self.session = request.session
        if session:
            self.session = session
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
        self.cart[p_id]['quantity'] += quantity
        self.save()

    # def add_product(self, product):
    #     self.cart[product.id] = {'product': product, 'price': product.price,
    #                              'quantity': 1, 'total_price': product.price}

    def subtract(self, product):
        p_id = str(product.id)
        if p_id in self.cart:
            self.cart[p_id]['quantity'] -= 1

    def remove(self, product, subtract=False):
        product_id = str(product.id)
        if subtract is False:
            if product_id in self.cart:
                del self.cart[product_id]
                self.save()
        else:
            if product_id in self.cart:
                if self.cart[product_id]['quantity'] == 1:
                    self.remove(product, subtract=False)
                else:
                    self.cart[product_id]['quantity'] -= 1
                    self.save()

    def count_products(self):
        return len(self.cart)

    def count_items(self):
        return sum([item['quantity'] for item in self.cart.values()])

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['quantity'] * Product.objects.filter(id=key).first().price) for key, item in self.cart.items())

    def get_all_items(self):
        return self.cart.keys()

    def get_products(self):
        return iter(self)

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def __len__(self):
        """Count all items"""
        return sum([item['quantity'] for item in self.cart.values()])

    def __iter__(self):
        """Iterate over cart products and get them from database"""
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
            cart[str(product.id)]['price'] = product.price
            cart[str(product.id)]['total_price'] = product.price * cart[str(product.id)]['quantity']


        for item in cart.values():
            yield item











