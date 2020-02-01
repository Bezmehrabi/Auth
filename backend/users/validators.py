import re
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


def validate_phonenumber(telnum: str):
    if not telnum.startswith('09'):
        msg = _('phone number is wrong.')
        raise ValidationError(msg)
