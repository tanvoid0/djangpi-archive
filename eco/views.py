from django.shortcuts import render
from rest_framework import viewsets
from .models import Datalog, Plant
from .serializers import DatalogSerializer, PlantSerializer


class DatalogView(viewsets.ModelViewSet):
    queryset = Datalog.objects.all()
    serializer_class = DatalogSerializer

class PlantView(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer