from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddNewProductForm
from shop.models import Product


def cart(request):
    cart = Cart(request)

    return render(request, 'cart/cart.html', {'cart': cart})

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = CartAddNewProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quanity=cd['quantity'], quantity_update=cd['update'])
            return redirect('cart:cart_detail')
        
