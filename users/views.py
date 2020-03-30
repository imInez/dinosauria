from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib.auth import views as auth_views
from .models import Profile, ShipmentAddress
from django.contrib.auth.decorators import login_required
from .forms import AddressModelForm, ProfileForm
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
        addresses = ShipmentAddress.objects.filter(profile=user_profile)
        if request.method == 'POST':
            address_form = AddressModelForm(request.POST)
            profile_form = ProfileForm(request.POST)
            # profile data update
            if request.POST.get('email') and profile_form.is_valid():
                cd = profile_form.cleaned_data
                user_profile.phone = cd.get('phone')
                user_profile.save()
            if address_form.is_valid():
                cd = address_form.cleaned_data
                # address update
                if request.POST.get('address_id'):
                    edited_address = [ad for ad in addresses if ad.id == cd.get('address_id')][0]
                else:
                    # new address creation
                    edited_address = ShipmentAddress()
                    cd['profile_id'] = user_profile.id
                # remove or update and save
                if request.POST.get('remove'):
                    edited_address.clean()
                    edited_address.delete()
                elif request.POST.get('set_main'):
                    print('SET MAIN')
                    edited_address.is_main = True
                    edited_address.save()
                else:
                    for key, value in cd.items():
                        print('CD: ', cd)
                        edited_address.__setattr__(key, value)
                    edited_address.save()
            return redirect('users:profile')
        else:
            address_forms = views_helpers.fill_many_addresses(request)
            profile_form = views_helpers.fill_profile(request)
            new_address_form = AddressModelForm()
        return render(request, 'users/profile.html', {'user_profile': user_profile, 'profile_form': profile_form,
                                                      'address_forms': address_forms,
                                                      'new_address_form': new_address_form,
                                                      'addresses': addresses})
    else:
        return render(request, 'users/login.html')

