from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Product
from django.views.decorators.http import require_POST


def cart_checkout(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})


@require_POST
def cart_add(request, product_id):
    form = CartAddProductForm(request.POST)
    add(request, product_id, form)
    return redirect('cart:cart_checkout')


# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect('cart:cart_checkout')



def add(request, product_id, form):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if form.is_valid():
        cd = form.cleaned_data
        print(cd)
        cart.add(product=product, quantity=cd['quantity'], quantity_update=cd['update'])


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    print(request.POST)
    if request.POST.get('single', False) == 'True':
        cart.remove(product, subtract=True)
    else:
        cart.remove(product)
    return redirect('cart:cart_checkout')