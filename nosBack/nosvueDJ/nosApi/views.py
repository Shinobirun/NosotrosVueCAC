from django.shortcuts import render
from .models import Usuario, PaqueteTuristico, HistorialViajes
from .serializers import UsuarioSerializer, PaqueteTuristicoSerializer, HistorialViajesSerializer
from rest_framework import generics

class UsuarioListView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PaqueteTuristicoListView(generics.ListCreateAPIView):
    queryset = PaqueteTuristico.objects.all()
    serializer_class = PaqueteTuristicoSerializer

class HistorialViajesListView(generics.ListCreateAPIView):
    queryset = HistorialViajes.objects.all()
    serializer_class = HistorialViajesSerializer
