from django.db import models

class Ruta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    origen = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    paradas = models.TextField()
    activa = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre