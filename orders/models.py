from django.db import models
from users.models import Profile, ShipmentAddress
from shop.models import Product
from django.utils import timezone

ORDER_STATUSES = [('NEW', 'NEW'), ('PAYONG', 'ONGOING PAYMENT'), ('PAYPRO', 'PAYMENT PROCESSED'),
                  ('INPROG', 'IN PROGRESS'), ('SENT', 'SENT'), ('DELIV', 'DELIVERED')]
PAYMENT_STATUSES = [('O', 'ONGOING'), ('S', 'SUCCESSFUL'), ('F', 'FAILED')]

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    quantity = models.IntegerField()


class Order(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(ShipmentAddress, on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(OrderProduct)
    created = models.DateTimeField()
    last_update = models.DateTimeField()
    status = models.CharField(max_length=6, choices=ORDER_STATUSES, default='NEW')
    payment_status = models.CharField(max_length=6, choices=PAYMENT_STATUSES, default='O')
    total = models.DecimalField(max_digits=10, decimal_places=2)

    payment_id = models.CharField(max_length=150, blank=True)


    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        self.last_update = timezone.now()
        return super(Order, self).save(*args, **kwargs)

    class Meta():
        ordering = ['-created']



