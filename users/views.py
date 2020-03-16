from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from .models import Profile

# Create your views here.



def create_user_profile(user, cd):
    profile = Profile()
    profile.user = user
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
            usr.save()
            create_user_profile(usr, cd)
            auth_views.auth_login(request, usr)
            return redirect(nxt)
    else:
        form = UserRegisterForm()
    return render(request, 'users/auth/registration.html', {'form': form})