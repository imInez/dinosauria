from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib.auth import views as auth_views
from .models import Profile, ShipmentAddress
from django.contrib.auth.decorators import login_required
from .forms import AddressModelForm, ProfileForm
from helpers import views_helpers
from cart.cart import Cart

cart = Cart(request)

def register(request):
    if request.method == 'POST':
        nxt = request.POST.get('next')
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            usr = form.save(commit=False)
            cd = form.cleaned_data
            usr.username = cd.get('email')
            usr.first_name = cd.get('name')
            usr.last_name = cd.get('surname')
            usr.save()
            views_helpers.create_user_profile(usr.id, cd)
            auth_views.auth_login(request, usr)
            return redirect(nxt)
    else:
        if request.user.is_authenticated:
            return profile(request)
        form = UserRegisterForm()
    return render(request, 'users/auth/registration.html', {'form': form, 'cart': cart})


@login_required(login_url='users:login')
def profile(request):
    user_profile = Profile.objects.filter(user=request.user).first()
    addresses = ShipmentAddress.objects.filter(profile=user_profile)
    if request.method == 'POST':
        address_form = AddressModelForm(request.POST)
        profile_form = ProfileForm(request.POST)
        # profile data update
        views_helpers.update_profile(request, user_profile, profile_form)
        # address data update
        views_helpers.update_address(request, address_form, addresses, user_profile)
        return redirect('users:profile')
    else:
        address_forms = views_helpers.fill_many_addresses(request)
        profile_form = views_helpers.fill_profile(request)
        new_address_form = AddressModelForm()
    return render(request, 'users/profile.html', {'user_profile': user_profile, 'profile_form': profile_form,
                                                  'address_forms': address_forms,
                                                  'new_address_form': new_address_form,
                                                  'cart': cart
                                                  })


