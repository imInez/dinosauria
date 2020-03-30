from django import template
from users.models import ShipmentAddress, Profile

register = template.Library()



@register.inclusion_tag('users/single_address.html')
def show_address(address_id):
    address = ShipmentAddress.objects.filter(id=address_id).first()
    return {'name': address.name, 'surname': address.surname,
            'street': address.street, 'building_flat': address.building_flat,
            'city': address.city, 'zipcode': address.zipcode}


