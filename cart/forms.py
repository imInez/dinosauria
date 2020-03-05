from django import forms


PRODUCT_QUANTITY_CHOICES = [str(i) for i in range (1, 11)]

class CartAddNewProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, corerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
