from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.encoding import python_2_unicode_compatible
from singlecharcore.managers import UserManager

@python_2_unicode_compatible
class User(AbstractBaseUser, PermissionsMixin):
    character_id = models.PositiveIntegerField(primary_key=True)
    character_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'character_name'
    REQUIRED_FIELDS = ['character_id']

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return self.get_short_name() + " (%s)" % self.character_id
    def get_short_name(self):
        return str(self.character_name)

    def __str__(self):
        return self.get_short_name()
