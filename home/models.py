from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import widgets

# Create your models here.


class CustomUser(AbstractUser):

    password1 = models.CharField(max_length=100,)
    password2 = models.CharField(max_length=100)
    address = models.TextField(max_length=200) 