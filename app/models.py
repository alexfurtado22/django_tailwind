from django.db import models
from django.contrib.auth.models import AbstractUser

TOUR_STATUS = (
    ("active", "Active"),
    ("inactive", "Inactive"),
)


class UserProfile(AbstractUser):
    pass


class Tour(models.Model):
    oringin_contry = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, default="")

    status = models.CharField(max_length=20, choices=TOUR_STATUS, default="active")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


# Create your models here.
