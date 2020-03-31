from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Product
from django.views.decorators.http import require_POST
from helpers import views_helpers
from users.forms import AddressForm, ProfileForm, AddressModelForm
from users.models import Profile, ShipmentAddress


def cart_checkout(request):
    cart = Cart(request)
    # empty cart
    if cart.count_items() == 0:
        return render(request, 'cart/empty_cart.html')

    # values update
    if request.method == 'POST':
        print('POST: ', request.POST)
        address_form = AddressModelForm(request.POST)
        profile_form = ProfileForm(request.POST)
        # registered user
        if request.user.is_authenticated:
            profile = Profile.objects.filter(user=request.user).first()
            addresses = ShipmentAddress.objects.filter(profile=profile)
            # profile data update
            views_helpers.update_profile(request, profile, profile_form)
            # address data update
            views_helpers.update_address(request, address_form, addresses, profile)

        else:
            # get existing or create guest profile
            if profile_form.is_valid() and address_form.is_valid():
                # update or create profile
                profile, created = Profile.objects.get_or_create(email=profile_form.cleaned_data.get('email'))
                views_helpers.update_profile_data(profile, profile_form)
                # create address
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
        address_forms = views_helpers.fill_many_addresses(request)
        profile_form = views_helpers.fill_profile(request)
    can_order = views_helpers.check_can_order(request)
    return render(request, 'cart/cart.html',
                  {'cart': cart,
                   'address_forms': address_forms, 'profile_form': profile_form,
                   'can_order': can_order,
                   })

# def cart_checkout(request):
#     cart = Cart(request)
#     # empty cart
#     if cart.count_items() == 0:
#         return render(request, 'cart/empty_cart.html')
#
#     # values update
#     if request.method == 'POST':
#         address_form = AddressForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#         # registered user
#         if request.user.is_authenticated:
#             profile = Profile.objects.filter(user_id=request.user.id).first()
#             address = ShipmentAddress.objects.filter(profile=profile).first() \
#                 if ShipmentAddress.objects.filter(profile=profile).first() else ShipmentAddress(profile=profile)
#             if profile_form.is_valid() and address_form.is_valid():
#                 cd = profile_form.cleaned_data
#                 profile.phone = cd.get('phone')
#                 profile.save()
#                 cd = address_form.cleaned_data
#                 for key, value in cd.items():
#                     address.__setattr__(key, value)
#                 address.save()
#             request.session['address'] = address.id
#         else:
#             # get existing or create guest profile
#             if profile_form.is_valid() and address_form.is_valid():
#                 cd = profile_form.cleaned_data
#                 if views_helpers.get_profile(cd.get('email')):
#                     profile = views_helpers.get_profile(cd.get('email'))
#                 else:
#                     profile = Profile()
#                     profile.email = cd.get('email')
#                 if not profile.phone:
#                     profile.phone = cd.get('phone')
#                     profile.save()
#                 address = ShipmentAddress(profile=profile)
#                 address.save()
#                 cd = address_form.cleaned_data
#                 request.session['guest_address'] = cd
#                 for key, value in cd.items():
#                     address.__setattr__(key, value)
#                 address.save()
#                 request.session['guest_profile_email'] = profile.email
#                 request.session['address'] = address.id
#         return redirect('cart:cart_checkout')
#     else:
#         # request.session['address'] = get_address(request)
#         address_form = views_helpers.fill_address(request)
#         profile_form = views_helpers.fill_profile(request)
#     can_order = views_helpers.check_can_order(request)
#     return render(request, 'cart/cart.html',
#                   {'cart': cart, 'address_form': address_form, 'profile_form': profile_form,
#                    'can_order': can_order,
#                    })



# def cart_checkout(request):
#     cart = Cart(request)
#     if cart.count_items() == 0:
#         return render(request, 'cart/empty_cart.html')
#     if request.method == 'POST':
#         address_form = AddressForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#         if request.user.is_authenticated:
#             profile = Profile.objects.filter(user_id=request.user.id).first()
#             # address = ShipmentAddress.objects.filter(profile=profile).first() \
#             #     if ShipmentAddress.objects.filter(profile=profile).first() else ShipmentAddress(profile=profile)
#             # if profile_form.is_valid() and address_form.is_valid():
#             #     views_helpers.update_profile(profile, profile_form)
#             #     cd = address_form.cleaned_data
#             #     for key, value in cd.items():
#             #         address.__setattr__(key, value)
#             #     address.save()
#             # request.session['address'] = address.id
#
#             if request.POST.get('email') and profile_form.is_valid():
#                 views_helpers.update_profile(user_profile, profile_form)
#         else:
#             # get existing or create guest profile
#             if profile_form.is_valid() and address_form.is_valid():
#                 cd = profile_form.cleaned_data
#                 if views_helpers.get_profile(cd.get('email')):
#                     profile = views_helpers.get_profile(cd.get('email'))
#                 else:
#                     profile = Profile()
#                     profile.email = cd.get('email')
#                 if not profile.phone:
#                     profile.phone = cd.get('phone')
#                     profile.save()
#                 address = ShipmentAddress(profile=profile)
#                 address.save()
#                 cd = address_form.cleaned_data
#                 request.session['guest_address'] = cd
#                 for key, value in cd.items():
#                     address.__setattr__(key, value)
#                 address.save()
#                 request.session['guest_profile_email'] = profile.email
#                 request.session['address'] = address.id
#         return redirect('cart:cart_checkout')
#     else:
#         # request.session['address'] = get_address(request)
#         address_form = views_helpers.fill_many_addresses(request)[0]
#         profile_form = views_helpers.fill_profile(request)
#         new_address_form = AddressModelForm()
#     can_order = views_helpers.check_can_order(request)
#     return render(request, 'cart/cart.html',
#                   {'cart': cart, 'address_form': address_form, 'profile_form': profile_form,
#                    'can_order': can_order,
#                    })


@require_POST
def cart_add(request, product_id):
    form = CartAddProductForm(request.POST)
    views_helpers.add(request, product_id, form)
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


