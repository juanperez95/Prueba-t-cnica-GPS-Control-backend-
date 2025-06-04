from django.shortcuts import render
from .models import Concesionario
from .serializers import ConcesionarioSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as st

# Crear la ruta para poder consumir de la API
class ApiConcesionario(APIView):
    # Generar el endpoint de la API
    def get(self, request):
        # Generar el listado de los objetos
        concesionarios = Concesionario.objects.all()[:10] # Traer los primeros 10 objetos
        # serializar el contenido de la base da tos
        serializer = ConcesionarioSerializer(concesionarios, many=True)
        
        return Response({'data':serializer.data}, status=st.HTTP_200_OK)
    
    # Generar el endpoint para crear un nuevo objeto
    def post(self, request):
        pass

    # Generar el endpoint para actualizar un objeto
    def put(self, request, pk):
        pass


    # Generar el endpoint para eliminar un objeto
    def delete(self, request, pk):
        pass