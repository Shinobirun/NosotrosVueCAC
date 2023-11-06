from django.urls import path
from .views import UsuarioListView, UsuarioDetailView, PaqueteTuristicoListView, PaqueteTuristicoDetailView, HistorialViajesListView, verificar_email_existente

urlpatterns = [
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'), 
    path('paquetes/', PaqueteTuristicoListView.as_view(), name='paquete-list'),
    path('paquetes/<int:pk>/', PaqueteTuristicoDetailView.as_view(), name='paquete-detail'), 
    path('viajes/', HistorialViajesListView.as_view(), name='viaje-list'),
    path('verificar-email/', verificar_email_existente, name='verificar_email_existente'),
]
