from rest_framework import serializers

from app_tech.models import Leadership, Structural


class LeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = '__all__'


class StructuralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structural
        fields = '__all__'

