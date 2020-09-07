from .models import Product
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from cart.cart import Cart


def home(request):
    cart = Cart(request)
    return render(request, 'shop/home.html', {'cart': cart})


def products(request):
    all_products = Product.objects.filter(available=True)
    cart_form = CartAddProductForm()
    cart = Cart(request)
    return render(request, 'shop/product/product-list.html', {'products': all_products, 'cart_form': cart_form, 'cart': cart})


def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_form = CartAddProductForm()
    cart = Cart(request)
    return render(request, 'shop/product/product-details.html', {'product': product, 'cart_form': cart_form, 'cart': cart})

