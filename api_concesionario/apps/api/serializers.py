from rest_framework import serializers
from .models import Concesionario

# Crear el serializer para la API de concesionario
class ConcesionarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Concesionario
        fields = '__all__'