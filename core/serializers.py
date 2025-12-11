# core/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Empresa, Equipo, Tecnico, PlanMantencion, OrdenTrabajo

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = "__all__"


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class TecnicoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(source="user", queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Tecnico
        fields = ("id", "user", "user_id", "nombre_completo", "especialidad", "telefono")


class PlanMantencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanMantencion
        fields = "__all__"


class OrdenTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenTrabajo
        fields = "__all__"
