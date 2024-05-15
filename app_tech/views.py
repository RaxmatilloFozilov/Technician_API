from django.http import HttpResponseForbidden
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import api_view, parser_classes
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from app_tech.models import Structural, Leadership, Standard, Electronic_Standard, Connection, Building, Dictionary
from app_tech.serializers import StructuralSerializer, LeadershipSerializer, StandardSerializer, ElectronicStandardSerializer, ConnectionSerializer, BuildingSerializer, DictionarySerializer


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


class ElectronicStandardViewSet(viewsets.ModelViewSet):
    queryset = Electronic_Standard.objects.all()
    serializer_class = ElectronicStandardSerializer
    permission_classes = [MultiPartParser]


class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    permission_classes = [MultiPartParser]


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [MultiPartParser]


class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    parser_classes = [MultiPartParser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DictionarySerializer
        return DictionarySerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return serializer.save


