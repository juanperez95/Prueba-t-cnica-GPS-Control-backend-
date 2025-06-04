from django.urls import path
from .views import ApiConcesionario

urlpatterns = [
    path('', ApiConcesionario.as_view(), name='api-concesionario'), # Ruta get para los datos de API
    path('<uuid:pk>', ApiConcesionario.as_view(), name='api-concesionario-crud'), # Ruta para eliminar o actualizar un objeto de la API
]
