from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True)
    surname = models.CharField(max_length=40, blank=True)
    street = models.CharField(max_length=50, blank=True)
    building_flat = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.user.email

