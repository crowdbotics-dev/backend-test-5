from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import BackendViewSet, New783ViewSet

router = DefaultRouter()
router.register("backend", BackendViewSet, basename="backend")
router.register("new783", New783ViewSet, basename="new783")

urlpatterns = [
    path("connectors/", include(router.urls)),
]
