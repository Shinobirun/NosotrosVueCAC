from .models import UserProfile, PaqueteTuristico, HistorialViajes
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class PaqueteTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaqueteTuristico
        fields= '__all__'

class HistorialViajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialViajes
        fields = '__all__'        

class ApiTokenObtainPairSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True, label="Username")
    description = serializers.CharField(max_length=255, required=True, label="Password")