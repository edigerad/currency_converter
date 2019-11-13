from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

from .managers import UserManager
from .validators import name_regex


class User(AbstractUser):
    first_name = models.CharField(_('first name'), validators=[name_regex],
                                  max_length=settings.FIRST_NAME_MAX_LENGTH,
                                  blank=False, null=True)
    last_name = models.CharField(_('last name'), validators=[name_regex],
                                 max_length=settings.LAST_NAME_MAX_LENGTH,
                                 blank=False, null=True)
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('first_name', 'last_name')

    def __str__(self):
        return f'id: {self.id} | username: {self.username} | email: {self.email}'

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        return self.first_name
