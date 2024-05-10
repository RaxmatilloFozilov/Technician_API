from django.urls import path

from rest_framework.routers import DefaultRouter

from app_tech.views import StructuralViewSet, LeadershipViewSet, StandardViewSet

router = DefaultRouter()
router.register(r'structural', StructuralViewSet)
router.register(r'leadership', LeadershipViewSet)
router.register(r'standard', StandardViewSet)


urlpatterns = router.urls

