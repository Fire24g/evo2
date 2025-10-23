from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, choices = [('Operativo', 'Operativo'), ('En reparacion', 'En reparacion'), ('Dado de baja', 'Dado de baja')], default='Operativo')
    fecha_ingreso = models.DateField()
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
