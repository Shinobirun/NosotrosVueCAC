from django.shortcuts import render
from .models import UserProfile, PaqueteTuristico, HistorialViajes
from .serializers import UsuarioSerializer, PaqueteTuristicoSerializer, HistorialViajesSerializer
from rest_framework  import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from rest_framework.response import Response


class UsuarioListView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
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
    queryset = UserProfile.objects.all()
    serializer_class = UsuarioSerializer

class PaqueteTuristicoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaqueteTuristico.objects.all()
    serializer_class = PaqueteTuristicoSerializer

def verificar_email_existente(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        if UserProfile.objects.filter(mail=email).exists():
            return JsonResponse({'existe': True})
        else:
            return JsonResponse({'existe': False})
        
@api_view(['POST'])
@permission_classes([AllowAny])
def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                'mensaje': 'Inicio de sesión exitoso',
                'access_token': access_token,
                'refresh_token': refresh_token,
            })

        return Response({'mensaje': 'Correo electrónico o contraseña incorrectos'}, status=400)

    return Response({'mensaje': 'Método no permitido'}, status=405)