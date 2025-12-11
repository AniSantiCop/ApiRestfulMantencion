from django.shortcuts import render

# core/views.py
from rest_framework import viewsets
from .models import Empresa, Equipo, Tecnico, PlanMantencion, OrdenTrabajo
from .serializers import (
    EmpresaSerializer,
    EquipoSerializer,
    TecnicoSerializer,
    PlanMantencionSerializer,
    OrdenTrabajoSerializer
)

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer


class PlanMantencionViewSet(viewsets.ModelViewSet):
    queryset = PlanMantencion.objects.all()
    serializer_class = PlanMantencionSerializer


class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
