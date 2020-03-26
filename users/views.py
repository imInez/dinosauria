from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib.auth import views as auth_views
from .models import Profile, ShipmentAddress
from django.contrib.auth.decorators import login_required
from .forms import AddressForm, ProfileForm
from helpers import views_helpers



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
    return render(request, 'users/auth/registration.html', {'form': form})


@login_required
def profile(request):
    if request.user.is_authenticated:
        user_profile = Profile.objects.filter(user=request.user).first()
        address_forms = views_helpers.fill_many_addresses(request)
        profile_form = views_helpers.fill_profile(request)
        return render(request, 'users/profile.html', {'user_profile': user_profile, 'address_forms': address_forms,
                                                      'profile_form': profile_form})
    else:
        return render(request, 'users/login.html')

