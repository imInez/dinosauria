from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=20, required=False)
    surname = forms.CharField(max_length=40, required=False)
    street = forms.CharField(max_length=50, required=False)
    building_flat = forms.CharField(max_length=10, required=False)
    city = forms.CharField(max_length=50, required=False)
    zipcode = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        widgets = {'username': forms.HiddenInput()}
        fields = ['email', 'password1', 'password2',
                  'name', 'surname', 'street', 'building_flat', 'city', 'zipcode']


