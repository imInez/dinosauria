from users.models import Profile, ShipmentAddress
from users.forms import ProfileForm, AddressForm
from cart.cart import Cart
from shop.models import Product
from django.shortcuts import get_object_or_404

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

def create_user_profile(user_id, cd):
    profile = Profile()
    profile.user_id = user_id
    profile.email = cd.get('email')
    profile.phone = cd.get('phone')
    profile.save()
    create_user_address(profile, cd)

def get_profile(email):
    profile = Profile.objects.filter(email=email).first()
    return profile


def get_address(request):
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


def validate(request, auth):
    if auth:
        profile = get_profile(request.user.email)
        address_values = has_address(request).values() if has_address(request) else []
    else:
        profile = get_profile(request.session.get('guest_profile_email'))
        address_values = request.session.get('guest_address')
    if profile and all([profile.email, profile.phone, all(address_values)]):
        return True
    return False


def check_can_order(request):
    if request.user.is_authenticated:
        enable = validate(request, True)
    else:
        enable = validate(request, False)
    return enable


def add(request, product_id, form):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if form.is_valid():
        cd = form.cleaned_data
        quantity = cd['quantity'] if cd['quantity'] else 1
        cart.add(product=product, quantity=quantity)
