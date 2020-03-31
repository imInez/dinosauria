from users.models import Profile, ShipmentAddress
from users.forms import ProfileForm, AddressModelForm
from cart.cart import Cart
from shop.models import Product
from django.shortcuts import get_object_or_404


# users
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


def create_user_profile(user_id, cd):
    profile = Profile()
    profile.user_id = user_id
    profile.email = cd.get('email')
    profile.phone = cd.get('phone')
    profile.save()
    if any([cd.get('name'),cd.get('surname'), cd.get('street'), cd.get('city')]):
        create_user_address(profile, cd)


def get_profile(email):
    profile = Profile.objects.filter(email=email).first()
    return profile


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


def update_profile_data(profile, profile_form):
    cd = profile_form.cleaned_data
    profile.phone = cd.get('phone')
    profile.save()


def update_profile(request, profile, profile_form):
    if request.POST.get('email') and profile_form.is_valid():
        update_profile_data(profile, profile_form)


def check_can_order(request):
    if request.user.is_authenticated:
        enable = validate(request, True)
    else:
        enable = validate(request, False)
    return enable


def validate(request, auth):
    if auth:
        profile = get_profile(request.user.email)
        address_values = [profile.shipmentaddress_set.filter(is_main=True).first()]
    else:
        profile = get_profile(request.session.get('guest_profile_email'))
        address_values = request.session.get('guest_address')
    if profile and all([profile.email, profile.phone, all(address_values)]):
        return True
    return False


# cart


def add(request, product_id, form):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if form.is_valid():
        cd = form.cleaned_data
        quantity = cd['quantity'] if cd['quantity'] else 1
        cart.add_product_to_cart(product=product, quantity=quantity)


# addresses


def get_address(request):
    return ShipmentAddress.objects.filter(profile=Profile.objects.filter(email=request.user.email).first().id)


def has_many_addresses(request):
    user_profile = Profile.objects.filter(user_id=request.user.id).first()
    user_addresses = ShipmentAddress.objects.filter(profile=user_profile)
    if user_addresses:
        addresses = []
        for address in user_addresses:
            address_fields = {'name': address.name, 'surname': address.surname, 'street': address.street,
                              'building_flat': address.building_flat, 'city': address.city,
                              'zipcode': address.zipcode, 'is_main': address.is_main,  'address_id': address.pk}
            if any(address_fields.values()):
                addresses.append(address_fields)
        return addresses
    else:
        return False


def fill_many_addresses(request):
    forms = []
    if request.user.is_authenticated:
        addresses_fields = has_many_addresses(request)
    elif request.session.get('guest_address'):
        addresses_fields = [request.session.get('guest_address')]
    else:
        return [AddressModelForm()]
    if addresses_fields:
        for address_fields in addresses_fields:
            form = AddressModelForm()
            for key, value in address_fields.items():
                form.fields[key].initial = value
            forms.append(form)
        return forms


# def has_address(request):
#     user_profile = Profile.objects.filter(user_id=request.user.id).first()
#     user_address = ShipmentAddress.objects.filter(profile=user_profile).first()
#     if user_address:
#         address_fields = {'name': user_address.name, 'surname': user_address.surname, 'street': user_address.street,
#                           'building_flat': user_address.building_flat, 'city': user_address.city,
#                           'zipcode': user_address.zipcode, 'is_main': user_address.is_main, }
#         if any(address_fields.values()):
#             return address_fields
#     else:
#         return False


def update_address(request, address_form, addresses, profile):
    if address_form.is_valid():
        cd = address_form.cleaned_data
        # address update
        if request.POST.get('address_id'):
            edited_address = [ad for ad in addresses if ad.id == cd.get('address_id')][0]
        else:
            # new address creation
            edited_address = ShipmentAddress()
            cd['profile_id'] = profile.id
        # remove or update and save
        if request.POST.get('remove'):
            edited_address.clean()
            edited_address.delete()
        elif request.POST.get('set_main'):
            for address in addresses:
                address.is_main = False
                address.save()
            edited_address.is_main = True
            edited_address.save()
        else:
            for key, value in cd.items():
                edited_address.__setattr__(key, value)
            edited_address.save()
