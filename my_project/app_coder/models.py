from django.db import models

# Create your models here.

"""
Hermano (nombre, apellido, edad, cumpleaños)
Padres (nombre, apellido, edad, cumpleaños)
"""

class Hermano(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    edad = models.IntegerField()
    cumpleaños = models.DateField()


class Padres(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    edad = models.IntegerField()
    cumpleaños = models.DateField()