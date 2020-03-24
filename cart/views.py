from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Product
from django.views.decorators.http import require_POST
from users.views import add_address, has_address, get_profile, add_profile
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
            ## get existing or create guest profile
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
        address_form = add_address(request)
        profile_form = add_profile(request)
    can_order = check_can_order(request)
    return render(request, 'cart/cart.html',
                  {'cart': cart, 'address_form': address_form, 'profile_form': profile_form,
                   'can_order': can_order,
                   })





# def cart_checkout(request):
#     cart = Cart(request)
#     if cart.count_items() == 0:
#         return render(request, 'cart/empty_cart.html')
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             address_form = AddressForm(request.POST)
#             profile_form = ProfileForm(request.POST)
#             # get existing or create guest profile
#             if profile_form.is_valid() and address_form.is_valid():
#                 cd = profile_form.cleaned_data
#                 if get_profile(cd.get('email')):
#                     guest_profile = get_profile(cd.get('email'))
#                 else:
#                     guest_profile = Profile()
#                     guest_profile.email = cd.get('email')
#                 if not guest_profile.phone:
#                     guest_profile.phone = cd.get('phone')
#                     guest_profile.save()
#                 user_address = ShipmentAddress(profile=guest_profile)
#                 user_address.save()
#                 cd = address_form.cleaned_data
#                 request.session['guest_address'] = cd
#                 for key, value in cd.items():
#                     user_address.__setattr__(key, value)
#                 user_address.save()
#                 request.session['guest_profile_email'] = guest_profile.email
#             # return redirect('cart:cart_checkout')
#         else:
#             profile_form = add_profile(request)
#             address_form = add_address(request)
#     else:
#         address_form = AddressForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#         user_profile = Profile.objects.filter(user_id=request.user.id).first()
#         user_address = ShipmentAddress.objects.filter(profile=user_profile).first()
#         if request.method == 'POST':
#             if profile_form.is_valid() and address_form.is_valid():
#                 cd = profile_form.cleaned_data
#                 profile = get_profile(request.user.email)
#                 profile.email = cd.get('email')
#                 profile.phone = cd.get('phone')
#                 profile.save()
#                 cd = address_form.cleaned_data
#                 for key, value in cd.items():
#                     user_address.__setattr__(key, value)
#                 user_address.save()
#             return redirect('cart:cart_checkout')
#         else:
#             address_form = add_address(request)
#             profile_form = add_profile(request)
#     can_order = check_can_order(request)
#     return render(request, 'cart/cart.html',
#                   {'cart': cart, 'address_form': address_form, 'profile_form': profile_form,
#                    'can_order': can_order,
#                    })


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


