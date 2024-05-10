from django.urls import path

from rest_framework.routers import DefaultRouter

from app_tech.views import StructuralViewSet, LeadershipViewSet

router = DefaultRouter()
router.register(r'structural', StructuralViewSet)
router.register(r'leadership', LeadershipViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('structural/', StructuralViewSet.as_view),
#     path('leadership/', LeadershipViewSet.as_view)
# ] + router.urls
