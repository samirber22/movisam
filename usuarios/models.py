from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    es_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username