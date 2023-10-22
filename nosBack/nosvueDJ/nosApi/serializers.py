from .models import Usuario, PaqueteTuristico, HistorialViajes
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PaqueteTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaqueteTuristico
        fields= '__all__'

class HistorialViajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialViajes
        fields = '__all__'        