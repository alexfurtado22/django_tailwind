from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from app.managers import UserProfileManager

TOUR_STATUS = (
    ("active", "Active"),
    ("inactive", "Inactive"),
)


class UserProfile(AbstractUser):
    email = models.EmailField("email_address", max_length=255, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserProfileManager()  # Custom manager

    @property
    def tour_count(self):
        return self.tours.count()


class Tour(models.Model):
    oringin_contry = models.CharField("Origin Country", max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, default="")

    status = models.CharField(max_length=20, choices=TOUR_STATUS, default="active")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tours"
    )

    @property
    def origin_country(self):
        return self.oringin_contry  # Alias for correct naming


# Create your models here.
