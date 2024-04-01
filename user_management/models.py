from django.db import models
from django.contrib.auth.models import AbstractUser
from .Managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=20,
        unique=True,
        help_text="Required. 20 or fewer character. Letters, digits, and spaces only",
        validators=[],
        error_messages={
            'unique':'Username not available.'
        }
    )

    email = models.EmailField(
        max_length=100,
        unique=True,
        validators=[],
        error_messages={
            'unique':'Email already exists.'
        }
    )

    phonenumber = models.CharField(
        max_length=15,
        unique=True,
        error_messages={
            'unique': 'Phone Number already exists.'
        }
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

