from django.shortcuts import render
from .models import Order, OrderProduct
from cart.cart import Cart
from users.models import ShipmentAddress
from users.views import get_profile

import time

def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        profile = get_profile(request.user.email) if request.user.is_authenticated \
            else get_profile(request.session.get('guest_profile_email'))
        new_order = Order()
        new_order.author = profile
        new_order.address = ShipmentAddress.objects.filter(id=request.session.get('address')).first()
        new_order.status = 'NEW'
        new_order.total = cart.get_total_price()
        new_order.save()

        for product in cart:
            new_order_product = OrderProduct(order=new_order, product=product.get('product'),
                                             price=product.get('price'), quantity=product.get('quantity'))
            new_order_product.save()
            new_order.products.add(new_order_product)

        new_order.save()
        cart.clear()

        return render(request, 'orders/success.html')
    else:
        pass
