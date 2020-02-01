from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, telnum, name, password=None, **kwargs):
        if not telnum:
            raise ValueError('user must have a phone number')
        user = self.model(telnum=telnum, name=name, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_admin = True
        user.save(using=self._db)
        return user