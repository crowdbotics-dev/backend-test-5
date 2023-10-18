from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import BackendViewSet

router = DefaultRouter()
router.register("backend", BackendViewSet, basename="backend")

urlpatterns = [
    path("connectors/", include(router.urls)),
]
