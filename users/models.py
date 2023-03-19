from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):

    CHOICE = [
        (True, 'True'),
        (False, 'False')
    ]

    username = None
    email = models.EmailField(_("email address"), unique=True, null=False)
    is_active = models.BooleanField(choices=CHOICE, default=True)
    position = models.CharField(max_length=20, null=False, blank=False)

    
    class Meta:
        ordering = ['-id']

    @property
    def generate_identication(self):
        unique_id = f"{self.first_name}-{self.phone}-{self.last_name}"
        return unique_id
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

