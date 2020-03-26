from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Product
from django.views.decorators.http import require_POST
from users.views import fill_address, has_address, get_address, get_profile, fill_profile
from users.forms import AddressForm, ProfileForm
from users.models import Profile, ShipmentAddress


def validate(request, auth):
    if auth:
        profile = get_profile(request.user.email)
        address_values = has_address(request).values() if has_address(request) else []
    else:
        profile = get_profile(request.session.get('guest_profile_email'))
        address_values = request.session.get('guest_address')
    if profile and all([profile.email, profile.phone, all(address_values)]):
        return True
    return False


def check_can_order(request):
    if request.user.is_authenticated:
        enable = validate(request, True)
    else:
        enable = validate(request, False)
    return enable


def cart_checkout(request):
    cart = Cart(request)
    if cart.count_items() == 0:
        return render(request, 'cart/empty_cart.html')
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if request.user.is_authenticated:
            profile = Profile.objects.filter(user_id=request.user.id).first()
            address = ShipmentAddress.objects.filter(profile=profile).first() \
                if ShipmentAddress.objects.filter(profile=profile).first() else ShipmentAddress(profile=profile)
            if profile_form.is_valid() and address_form.is_valid():
                cd = profile_form.cleaned_data
                profile.phone = cd.get('phone')
                profile.save()
                cd = address_form.cleaned_data
                for key, value in cd.items():
                    address.__setattr__(key, value)
                address.save()
            request.session['address'] = address.id
        else:
            # get existing or create guest profile
            if profile_form.is_valid() and address_form.is_valid():
                cd = profile_form.cleaned_data
                if get_profile(cd.get('email')):
                    profile = get_profile(cd.get('email'))
                else:
                    profile = Profile()
                    profile.email = cd.get('email')
                if not profile.phone:
                    profile.phone = cd.get('phone')
                    profile.save()
                address = ShipmentAddress(profile=profile)
                address.save()
                cd = address_form.cleaned_data
                request.session['guest_address'] = cd
                for key, value in cd.items():
                    address.__setattr__(key, value)
                address.save()
                request.session['guest_profile_email'] = profile.email
                request.session['address'] = address.id
        return redirect('cart:cart_checkout')
    else:
        # request.session['address'] = get_address(request)
        address_form = fill_address(request)
        profile_form = fill_profile(request)
    can_order = check_can_order(request)
    return render(request, 'cart/cart.html',
                  {'cart': cart, 'address_form': address_form, 'profile_form': profile_form,
                   'can_order': can_order,
                   })


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
        quantity = cd['quantity'] if cd['quantity'] else 1
        cart.add(product=product, quantity=quantity)


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.POST.get('single', False) == 'True':
        cart.remove(product, subtract=True)
    else:
        cart.remove(product)
    return redirect('cart:cart_checkout')


