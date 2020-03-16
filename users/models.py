from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)
    street = models.CharField(max_length=50)
    building_flat = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)


