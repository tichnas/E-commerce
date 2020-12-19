from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)

    class Type(models.TextChoices):
        JEWELLERY = "JEWELLERY"
        CLOTH = "CLOTH"

    type = models.CharField(max_length=50, choices=Type.choices)
    description = models.TextField()

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(
        default=False, help_text=_("Designates if a user can log into this admin site")
    )
    phone = models.IntegerField(
        validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)]
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["name", "phone"]

    objects = UserManager()


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(_("Address name"), max_length=255)
    address1 = models.CharField(_("Address Line 1"), max_length=255)
    address2 = models.CharField(_("Address Line 2"), max_length=255)
    pincode = models.IntegerField(
        validators=[MinValueValidator(100000), MaxValueValidator(999999)]
    )
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)