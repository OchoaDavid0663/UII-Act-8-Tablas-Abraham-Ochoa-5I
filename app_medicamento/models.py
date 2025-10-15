
from django.db import models

class Medicamento(models.Model):
    nombre = models.CharField(max_length=50)
    funcion = models.CharField(max_length=100)
    presentacion = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return f'Medicamento: {self.nombre} {self.funcion}'
