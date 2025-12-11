# core/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    EmpresaViewSet,
    EquipoViewSet,
    TecnicoViewSet,
    PlanMantencionViewSet,
    OrdenTrabajoViewSet
)

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'equipos', EquipoViewSet)
router.register(r'tecnicos', TecnicoViewSet)
router.register(r'planes-mantencion', PlanMantencionViewSet)
router.register(r'ordenes-trabajo', OrdenTrabajoViewSet)

@api_view(["GET"])
def health(request):
    return Response({"status": "ok", "message": "API funcionando"})

urlpatterns = [
    path("", include(router.urls)),
    path("health/", health, name="health"),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
