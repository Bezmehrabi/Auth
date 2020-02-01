import random

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser

from django.core.validators import MinLengthValidator
from .managers import CustomUserManager
from .validators import validate_phonenumber
from django.utils.translation import gettext_lazy as _


def gen_unique_random():
    while True:
        rand = random.randint(32453243, 97687656)
        if not get_user_model().objects.filter(code=rand):
            break
    return rand

class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(TimeStamp, AbstractBaseUser):
    telnum = models.CharField(verbose_name=_('Phone Number'), max_length=11, unique=True,
                              validators=[MinLengthValidator(11, message=''), validate_phonenumber])

    name = models.CharField(verbose_name=_('Name') ,max_length=32)

    code = models.IntegerField(editable=False, unique=True)
    rec_code = models.CharField(verbose_name=_('Recommender code'), max_length=24, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'telnum'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'کاربر'

    def __str__(self):
        print(self.__class__)
        return self.telnum

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_active

    @property
    def is_staff(self):
        return self.is_admin
    
    def save(self, *args, **kwargs):
        code = gen_unique_random()
        self.code = code
        super().save()
