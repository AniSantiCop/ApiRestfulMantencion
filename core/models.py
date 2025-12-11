# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField(blank=True)
    rut = models.CharField(max_length=20, unique=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Equipo(models.Model):
    empresa = models.ForeignKey(Empresa, related_name="equipos", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    numero_serie = models.CharField(max_length=100, unique=True)
    critico = models.BooleanField(default=False)
    fecha_instalacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.numero_serie}"


class Tecnico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil_tecnico")
    nombre_completo = models.CharField(max_length=200)
    especialidad = models.CharField(max_length=150)
    telefono = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.nombre_completo


class PlanMantencion(models.Model):
    equipo = models.ForeignKey(Equipo, related_name="planes", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    frecuencia_dias = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.equipo.numero_serie})"


class OrdenTrabajo(models.Model):
    ESTADOS = [
        ("PENDIENTE", "Pendiente"),
        ("PROGRAMADA", "Programada"),
        ("EN_PROGRESO", "En progreso"),
        ("COMPLETADA", "Completada"),
        ("CANCELADA", "Cancelada"),
    ]

    equipo = models.ForeignKey(Equipo, related_name="ordenes_trabajo", on_delete=models.CASCADE)
    plan = models.ForeignKey(PlanMantencion, related_name="ordenes_trabajo", null=True, blank=True, on_delete=models.SET_NULL)
    tecnico = models.ForeignKey(Tecnico, related_name="ordenes_trabajo", null=True, blank=True, on_delete=models.SET_NULL)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="PENDIENTE")
    fecha_programada = models.DateField(null=True, blank=True)
    completada_en = models.DateTimeField(null=True, blank=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"OT #{self.id} - {self.equipo.numero_serie}"

