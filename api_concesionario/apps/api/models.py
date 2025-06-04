from django.db import models
import uuid

# Crear el modelo para la API de concesionario
class Concesionario(models.Model):

    # Meta datos del modelo
    class Meta:
        verbose_name = 'Concesionario'


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # que el id no sea secuencial por seguridad en la base da datos
    marca = models.CharField(max_length=100, blank=True, null=True)
    surcursal = models.CharField(max_length=100, blank=True, null=True)
    aspirante = models.CharField(max_length=100, blank=True, null=True)


    # Respresentar el objeto con la siguiente informacion
    def __str__(self):
        return f"{self.marca} -> {self.aspirante}"