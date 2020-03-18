from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Product
from django.views.decorators.http import require_POST
from users.views import add_address
from users.forms import AddressForm
from users.models import Profile


def cart_checkout(request):
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            cd = address_form.cleaned_data
            user_profile = Profile.objects.filter(user_id=request.user.id).first()
            for key, value in cd.items():
                user_profile.__setattr__(key, value)
            user_profile.save()
        return redirect('cart:cart_checkout')
    cart = Cart(request)
    address_form = add_address(request)
    if cart.count_items() == 0:
        return render(request, 'cart/empty_cart.html')
    return render(request, 'cart/cart.html', {'cart': cart, 'address_form': address_form})
    # return render(request, 'cart/cart.html', {'cart': cart, 'form': form} if form else {'cart': cart})


@require_POST
def cart_add(request, product_id):
    form = CartAddProductForm(request.POST)
    add(request, product_id, form)
    return redirect('cart:cart_checkout')


def add(request, product_id, form):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'])


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.POST.get('single', False) == 'True':
        cart.remove(product, subtract=True)
    else:
        cart.remove(product)
    return redirect('cart:cart_checkout')


