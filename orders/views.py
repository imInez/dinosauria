from django.shortcuts import redirect
from django.urls import reverse
from .models import Order
from cart.cart import Cart
from helpers.views_helpers import get_profile
from django.views.decorators.http import require_POST


def clear_session(request, var):
    if request.session.get(var):
        del request.session[var]


@require_POST
def create_order(request):
    cart = Cart(request)
    profile = get_profile(request.user.email) if request.user.is_authenticated \
        else get_profile(request.session.get('guest_profile_email'))
    new_order = Order()
    new_order.author = profile
    new_order.address = profile.shipmentaddress_set.filter(profile=profile).filter(is_main=True).first()
    new_order.status = 'NEW'
    new_order.total = cart.get_total_price()
    new_order.save()
    for product in cart:
        new_order_product = new_order.products.create(order=new_order, product=product.get('product'),
                                         price=product.get('price'), quantity=product.get('quantity'))
    new_order.save()

    cart.clear()
    clear_session(request, 'guest_profile_email')
    clear_session(request, 'address')
    request.session['order_id'] = new_order.id

    return redirect(reverse('payments:in-progress'))


