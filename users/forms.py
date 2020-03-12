from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=40)
    street = forms.CharField(max_length=50)
    building_flat = forms.CharField(max_length=10)
    city = forms.CharField(max_length=50)
    zipcode = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2',
                  'name', 'surname', 'street', 'building_flat', 'city', 'zipcode']