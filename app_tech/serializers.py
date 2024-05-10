from rest_framework import serializers

from app_tech.models import Leadership, Structural, Standard


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
