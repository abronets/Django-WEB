from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model.
    """

    first_name = models.CharField(_('First name'), max_length=50)
    last_name = models.CharField(_('Last name'), max_length=50)
    email = models.EmailField(_('Email'), null=True, blank=True, unique=True)
    date_joined = models.DateTimeField(_('Date joined'), auto_now_add=True)
    is_staff = models.BooleanField(_('Is staff'), default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_short_name(self):
        return self.first_name

    def can_create_posts(self):
        if self.is_staff:
            return True
        else:
            return False

    @property
    def get_full_name(self):
        """
        Returns user's first and last name concatenation
        """
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('Користувач')
        verbose_name_plural = _('Користувачі')
        ordering = ('-date_joined',)
