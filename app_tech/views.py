from django.http import HttpResponseForbidden
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import api_view, parser_classes
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from app_tech.models import Structural, Leadership, Standard
from app_tech.serializers import StructuralSerializer, LeadershipSerializer, StandardSerializer


class StructuralViewSet(viewsets.ModelViewSet):
    queryset = Structural.objects.all()
    serializer_class = StructuralSerializer
    permission_classes = [MultiPartParser]


class LeadershipViewSet(viewsets.ModelViewSet):
    queryset = Leadership.objects.all()
    serializer_class = LeadershipSerializer
    permission_classes = [MultiPartParser]


class StandardViewSet(viewsets.ModelViewSet):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer
    permission_classes = [MultiPartParser]

