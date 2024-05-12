from rest_framework import serializers

from app_tech.models import Leadership, Structural, Standard, Connection, Building, Electronic_Standard


class LeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = '__all__'


class StructuralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structural
        fields = '__all__'


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'

        # fields = ['address', 'city', 'email', 'phone', 'FIO', 'leadership', 'text', 'comments']


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

        # fields = ['number', 'characters', 'name']


class ElectronicStandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electronic_Standard
        fields = '__all__'
        # fields = ['keyword', 'document_number', 'document_category', 'document_year', 'conditional_symbol']