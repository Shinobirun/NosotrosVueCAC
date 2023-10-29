from django.shortcuts import render
from .models import Usuario, PaqueteTuristico, HistorialViajes
from .serializers import UsuarioSerializer, PaqueteTuristicoSerializer, HistorialViajesSerializer
from rest_framework import generics

class UsuarioListView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PaqueteTuristicoListView(generics.ListCreateAPIView):
    serializer_class = PaqueteTuristicoSerializer

    def get_queryset(self):
        tipo = self.request.query_params.get('tipo')
        id = self.request.query_params.get('id')
        valor = self.request.query_params.get('valor')

        if tipo:
            return PaqueteTuristico.objects.filter(tipo=tipo)
        elif id:
            return PaqueteTuristico.objects.filter(id=id)
        elif valor:
            return PaqueteTuristico.objects.filter(valor=valor)

        return PaqueteTuristico.objects.all()

class HistorialViajesListView(generics.ListCreateAPIView):
    queryset = HistorialViajes.objects.all()
    serializer_class = HistorialViajesSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PaqueteTuristicoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaqueteTuristico.objects.all()
    serializer_class = PaqueteTuristicoSerializer
