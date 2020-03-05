from .models import Product
from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, 'shop/home.html')

def products(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product/product-list.html', {'products': products})

def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    # form to add to cart
    return render(request, 'shop/product/product-details.html', {'product': product})

