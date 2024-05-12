from django.urls import path

from rest_framework.routers import DefaultRouter

from app_tech.views import StructuralViewSet,LeadershipViewSet, StandardViewSet, ConnectionViewSet, ElectronicStandardViewSet, BuildingViewSet

router = DefaultRouter()
router.register(r'structural', StructuralViewSet)
router.register(r'leadership', LeadershipViewSet)
router.register(r'standard', StandardViewSet)
router.register(r'connection', ConnectionViewSet)
router.register(r'electronic_standard', ElectronicStandardViewSet)
router.register(r'building', BuildingViewSet)


urlpatterns = router.urls

