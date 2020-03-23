from django.db import models
from users.models import Profile
from shop.models import Product


ORDER_STATUSES = {'NEW': 'NEW', 'PAYONG': 'ONGOING PAYMENT', 'PAYPRO': 'PAYMENT PROCESSED', 'INPROG': 'IN PROGRESS',
                  'SENT': 'SENT', 'DELIV': 'DELIVERED'}
PAYMENT_STATUSES = {'S': 'SUCCESSFUL', 'F': 'FAILED'}


class Order(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    product = models.ManyToManyField(Product)
    created = models.DateTimeField()
    last_updated = models.DateTimeField()
    status = models.CharField(max_length=6, choices=ORDER_STATUSES, default='NEW')
    payment_status = models.CharField(max_length=6, choices=PAYMENT_STATUSES, default='F')
