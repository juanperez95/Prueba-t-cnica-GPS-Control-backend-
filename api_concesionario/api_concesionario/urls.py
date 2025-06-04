
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/concesionario/', include('apps.api.urls')), # Llamar las rutas de la aplicacion API
]