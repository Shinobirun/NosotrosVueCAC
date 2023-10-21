from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)
    gasto_total = models.DecimalField(max_digits=10, decimal_places=2)

class PaqueteTuristico(models.Model):
    titulo = models.CharField(max_length=100)
    informacion = models.CharField(max_length=500)
    foto_url = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50)

class HistorialViajes(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    paquete_turistico = models.ForeignKey(PaqueteTuristico, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha= models.DateField()