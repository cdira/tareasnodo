
from django.db import models
import datetime

# Create your models here.
class Escuela(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    #asignatura = models.ManyToManyField(Asignatura)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField(verbose_name="Mail del profesor")
    fecha_contratacion = models.DateField(datetime.date.today())
    #clave = models.CharField(max_length=8)
    #escuela = models.ForeignKey(Escuela, null=True, on_delete=models.CASCADE)
    escuela = models.OneToOneField(Escuela, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.apellido


class Asignatura(models.Model):
    nombre = models.CharField(max_length=20)
    profesor = models.OneToOneField(Profesor, null=True, on_delete=models.SET_NULL)
    escuela = models.ManyToManyField(Escuela)

    def __str__(self):
        return self.nombre

class RegistroProfesorEscuela(models.Model):
    profesor = models.ForeignKey(Profesor, null=True, on_delete=models.SET_NULL)
    escuela = models.ForeignKey(Escuela, null=True, on_delete=models.SET_NULL)
    horas = models.IntegerField(null=True)
    detalle = models.TextField(max_length=200, null=True)
    

    