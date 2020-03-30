from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Product
from django.views.decorators.http import require_POST
from helpers.views_helpers import fill_address, has_address, get_profile, fill_profile, validate, check_can_order, add, fill_many_addresses, has_many_addresses
from users.forms import AddressForm, ProfileForm
from users.models import Profile, ShipmentAddress


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
        address_form = fill_many_addresses(request)[0]
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


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.POST.get('single', False) == 'True':
        cart.remove(product, subtract=True)
    else:
        cart.remove(product)
    return redirect('cart:cart_checkout')


