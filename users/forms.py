from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ShipmentAddress

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False, max_length=20)
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
                  'phone', 'name', 'surname', 'street', 'building_flat', 'city', 'zipcode']


class AddressForm(forms.Form):
    name = forms.CharField(max_length=20, required=False)
    surname = forms.CharField(max_length=40, required=False)
    street = forms.CharField(max_length=50, required=False)
    building_flat = forms.CharField(max_length=10, required=False)
    city = forms.CharField(max_length=50, required=False)
    zipcode = forms.CharField(max_length=10, required=False)


class AddressModelForm(forms.ModelForm):
    address_id = forms.IntegerField(required=False, widget=forms.HiddenInput, label='')



    class Meta:
        model = ShipmentAddress
        fields = ('name', 'surname', 'street', 'building_flat', 'city', 'zipcode', 'is_main', 'address_id')
        labels = {'is_main': 'My shipment address', 'address_id': ''}
        # widgets = {'is_main': forms.HiddenInput}


class ProfileForm(forms.Form):
    email = forms.EmailField()
    phone = forms.CharField(max_length=12)