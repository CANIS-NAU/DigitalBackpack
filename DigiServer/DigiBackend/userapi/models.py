from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    username = models.CharField(max_length=250,blank=True, null=True,unique=True)
    email = models.EmailField(_('email address'), unique=True)
    password2 = models.CharField(max_length=250, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    roll = models.IntegerField(unique=True)
    phone = PhoneNumberField(default=None)
    address = models.CharField(max_length=255)
    subject = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['roll']