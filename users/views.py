from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import AddressForm

def create_user_profile(user_id, cd):
    profile = Profile()
    profile.user_id = user_id
    profile.name = cd.get('name')
    profile.surname = cd.get('surname')
    profile.street = cd.get('street')
    profile.building_flat = cd.get('building_flat')
    profile.city = cd.get('city')
    profile.zipcode = cd.get('zipcode')
    profile.save()


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
            create_user_profile(usr.id, cd)
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
        return render(request, 'users/profile.html', {'user_profile': user_profile})
    else:
        return render(request, 'users/login.html')


def add_address(request):
    form = AddressForm()
    if not request.user.id or not has_address(request, request.user.id):
        return form
    else:
        address_fields = has_address(request, request.user.id)
        for key, value in address_fields.items():
            form.fields[key].initial = value
    return form


def has_address(request, user_id):
    user_profile = Profile.objects.filter(user_id=user_id).first()
    address_fields = {'name': user_profile.name, 'surname': user_profile.surname, 'street': user_profile.street,
                      'building_flat': user_profile.building_flat, 'city': user_profile.city,
                      'zipcode': user_profile.zipcode}
    if all(address_fields) or any(address_fields):
        return address_fields
    else:
        return False