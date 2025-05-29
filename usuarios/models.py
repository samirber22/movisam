from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    es_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.username
# Create your models here.
