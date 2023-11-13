from django.shortcuts import render
from .models import UserProfile, PaqueteTuristico, HistorialViajes
from .serializers import UsuarioSerializer, PaqueteTuristicoSerializer, HistorialViajesSerializer
from rest_framework  import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.contrib.auth import authenticate, login


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
@permission_classes([AllowAny])   #Permite el acceso a esta vista sin autentificación      
        
def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.data.get('email')
        contrasena = request.data.get('contrasena')
        user = authenticate(request, username=email, password=contrasena)

        if user is not None:
            # Autenticación exitosa, generar tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Puedes guardar estos tokens en el frontend (por ejemplo, en el local storage)
            # y enviar el access_token con cada solicitud posterior para autenticar al usuario

            login(request, user)
            return JsonResponse({
                'mensaje': 'Inicio de sesión exitoso',
                'access_token': access_token,
                'refresh_token': refresh_token,
            })
        else:
            return JsonResponse({'mensaje': 'Correo electrónico o contraseña incorrectos'}, status=400)

    return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

