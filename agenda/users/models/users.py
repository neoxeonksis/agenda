# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from agenda.utils.models import CommonModel


class User(CommonModel, AbstractUser):

    email = models.EmailField(
        'Direccion de correo',
        unique=True,
        error_messages={
            'unique': 'Este campo es requerido'
        }
    )

    telefono = models.CharField(max_length=17, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

