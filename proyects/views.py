from django.shortcuts import render
from rest_framework import viewsets
from .models import Proyect
from .serializers import ProyectSerializer

class ProyectViewSet(viewsets.ModelViewSet):
    queryset = Proyect.objects.all()
    serializer_class = ProyectSerializer

# Create your views here.
