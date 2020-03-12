from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views


# Create your views here.

def register(request):
    if request.method == 'POST':
        nxt = request.POST.get('next')
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            tmp = form.save(commit=False)
            tmp.username = form.cleaned_data.get('email')
            tmp.save()
            auth_views.auth_login(request, tmp)
            return redirect(nxt)
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {'form': form})