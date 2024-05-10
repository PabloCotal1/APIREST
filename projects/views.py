from django.shortcuts import render
from rest_framework.views import apiView
from rest_framework.response import Response
from rest_framework import status
from .models import Project
# Create your views here.


class delete(APIView):
    def delete(self, request, pk):
        # Obtener el objeto a eliminar
        try:
            objeto = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({"detail": "El recurso no existe."}, status=status.HTTP_404_NOT_FOUND)

        # Eliminar el objeto
        objeto.delete()
        return Response({"detail": "Recurso eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
