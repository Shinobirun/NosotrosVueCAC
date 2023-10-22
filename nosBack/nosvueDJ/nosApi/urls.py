from django.urls import path
from .views import UsuarioListView, PaqueteTuristicoListView, HistorialViajesListView

urlpatterns = [
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('paquetes/', PaqueteTuristicoListView.as_view(), name='paquete-list'),
    path('viajes/', HistorialViajesListView.as_view(), name='viaje-list'),
]
