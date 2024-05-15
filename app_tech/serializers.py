from rest_framework import serializers

from app_tech.models import Leadership, Structural, Standard, Connection, Building, Electronic_Standard, Dictionary


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


class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('id', 'standard_number',)


    def standard_number(self,obj):
        try:
            lang = self.context['request'].GET.get['language']
            if lang == 'en':
                return obj.language_en
            elif lang == 'uz':
                return obj.language_uz
            elif lang == 'ru':
                return obj.language_ru
            elif lang == 'turk':
                return obj.language_turk

        except:
            return obj.language_uz




