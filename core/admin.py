# core/admin.py
from django.contrib import admin
from .models import Empresa, Equipo, Tecnico, PlanMantencion, OrdenTrabajo

admin.site.register(Empresa)
admin.site.register(Equipo)
admin.site.register(Tecnico)
admin.site.register(PlanMantencion)
admin.site.register(OrdenTrabajo)
