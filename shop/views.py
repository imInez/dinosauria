from .models import Product
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm

def home(request):
    return render(request, 'shop/home.html')

def products(request):
    products = Product.objects.filter(available=True)
    cart_form = CartAddProductForm()
    return render(request, 'shop/product/product-list.html', {'products': products, 'cart_form': cart_form})

def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_form = CartAddProductForm()
    return render(request, 'shop/product/product-details.html', {'product': product, 'cart_form': cart_form})

