from django.db import models
from django.urls import reverse
import psycopg2


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to=f'img/product', default='../static/img/logo-img-light-green.png')
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('shop:product_details', args=[self.id, self.slug])

    def __str__(self):
        return self.name







