from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from .models import Profile, ShipmentAddress
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import AddressForm, ProfileForm


def create_user_profile(user_id, cd):
    profile = Profile()
    profile.user_id = user_id
    profile.email = cd.get('email')
    profile.phone = cd.get('phone')
    profile.save()
    create_user_address(profile, cd)


def create_user_address(profile, cd):
    if any(cd):
        address = ShipmentAddress()
        address.profile = profile
        address.name = cd.get('name')
        address.surname = cd.get('surname')
        address.street = cd.get('street')
        address.building_flat = cd.get('building_flat')
        address.city = cd.get('city')
        address.zipcode = cd.get('zipcode')
        address.save()
        profile_ = Profile.objects.filter(user=profile.user).first()
        profile_.address = address
        profile_.save()


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


def get_profile(email):
    profile = Profile.objects.filter(email=email).first()
    return profile


def get_address(request):
    # email = get_profile(request.user.email)
    # print('PROFILE: ', email)
    return ShipmentAddress.objects.filter(profile=Profile.objects.filter(email=request.user.email).first().id)


def fill_profile(request):
    if request.user.is_authenticated:
        profile_ = Profile.objects.filter(email=request.user.email).first()
    else:
        profile_ = Profile.objects.filter(email=request.session.get('guest_profile_email', None)).first()
    form = ProfileForm()
    if profile_:
        form.fields['email'].initial = profile_.email
        form.fields['email'].readonly = True
        form.fields['phone'].initial = profile_.phone
    return form


def fill_address(request):
    form = AddressForm()
    if request.user.is_authenticated:
        address_fields = has_address(request)
    elif request.session.get('guest_address'):
        address_fields = request.session.get('guest_address')
    else:
        return form
    if address_fields:
        for key, value in address_fields.items():
            form.fields[key].initial = value
    return form


def has_address(request):
    user_profile = Profile.objects.filter(user_id=request.user.id).first()
    user_address = ShipmentAddress.objects.filter(profile=user_profile).first()
    if user_address:
        address_fields = {'name': user_address.name, 'surname': user_address.surname, 'street': user_address.street,
                          'building_flat': user_address.building_flat, 'city': user_address.city,
                          'zipcode': user_address.zipcode}
        if any(address_fields.values()):
            return address_fields
    else:
        return False