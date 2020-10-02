from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.crypto import get_random_string

def make_random_username(length, allowed_chars):
    import string
    return get_random_string(length=length, allowed_chars=allowed_chars)

class UserManager(UserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        username = self.make_random_username()
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        username = self.make_random_username()

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

    def make_random_username(self):
        import string
        return make_random_username(length=14, allowed_chars=string.ascii_lowercase)


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        unique=True,
    )

    objects = UserManager()

    # EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
