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
        try:        
            # Validar que los datos no lleguen vacios
            if request.data['marca'] != "" and request.data['surcursal'] != "" and request.data['aspirante'] != "":
                concesionario = ConcesionarioSerializer(data=request.data) # Crear el dato que llega de VUE
                if concesionario.is_valid(): # Validar que el dato sea valido
                    concesionario.save() # Guardar el objeto
                return Response({'data':True}, status=st.HTTP_201_CREATED)
            return Response({'data':False}, status=st.HTTP_400_BAD_REQUEST) # Devolver una mala respuesta
        except Exception as e:
            pass
        return Response({'data':False}, status=st.HTTP_400_BAD_REQUEST) # Devolver una mala respuesta

    # Generar el endpoint para actualizar un objeto
    def put(self, request, pk):
        try:
            concesionario = Concesionario.objects.get(pk=pk) # Obtener el objeto
            # Validar que los datos no lleguen vacios
            if request.data['marca'] != "" and request.data['surcursal'] != "" and request.data['aspirante'] != "":
                concesionario.marca = request.data['marca'] # Actualizar el objeto
                concesionario.surcursal = request.data['surcursal'] # Actualizar el objeto
                concesionario.aspirante = request.data['aspirante'] # Actualizar el objeto
                concesionario.save() # Guardar el objeto
                return Response({'update':True}, status=st.HTTP_200_OK)
        except Exception as e:
            return Response({'update':False}, status=st.HTTP_400_BAD_REQUEST) # Devolver una mala respuesta
        


    # Generar el endpoint para eliminar un objeto
    def delete(self, request, pk):
        try:
            Concesionario.objects.get(pk=pk).delete() # Eliminar el objeto
            return Response({'delete':True}, status=st.HTTP_200_OK)
        except Exception as e:
            return Response({'delete':False}, status=st.HTTP_400_BAD_REQUEST) # Devolver una mala respuesta
        