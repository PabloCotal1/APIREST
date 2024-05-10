from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ProjectViewSet

# Definir el enrutador
router = DefaultRouter()
router.register('projects', ProjectViewSet)

# Definir las URLs
urlpatterns = [
    # Incluir las URLs del enrutador
    path('api/', include(router.urls)),
]

