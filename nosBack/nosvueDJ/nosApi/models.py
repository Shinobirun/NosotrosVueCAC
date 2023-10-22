from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=50)
    puntos = models.DecimalField(max_digits=10, decimal_places=0)

class PaqueteTuristico(models.Model):
    titulo = models.CharField(max_length=100)
    informacion = models.CharField(max_length=500)
    foto_url = models.CharField(max_length=255, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50, null=True, blank=True)

class HistorialViajes(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='historial_viajes')
    paquete_turistico = models.ForeignKey(PaqueteTuristico, on_delete=models.CASCADE, related_name='historial_viajes')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
