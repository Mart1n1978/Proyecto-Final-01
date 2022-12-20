from django.db import models

class Familiar(models.Model):

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
          
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

class Automovil(models.Model):

    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    año = models.CharField(max_length=200)
          
    def __str__(self):
      return f"{self.marca}, {self.modelo}, {self.año}"

class Mascota(models.Model):

    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=200)
    edad = models.IntegerField()
          
    def __str__(self):
      return f"{self.nombre}, {self.raza}, {self.edad}"