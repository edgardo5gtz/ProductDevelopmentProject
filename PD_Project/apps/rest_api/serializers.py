from rest_framework import serializers
from ..Risks.models import *


class TextFieldSerializer(serializers.ModelSerializer):
    """ Return TextFieldVal model serialized data"""
    class Meta:
        model = TextFieldVal
        fields = '__all__'


class EnumFieldSerializer(serializers.ModelSerializer):
    """ Return EnumFieldVal model serialized data"""
    class Meta:
        model = EnumFieldVal
        fields = '__all__'


class DateFieldSerializer(serializers.ModelSerializer):
    """ Return DateFieldVal model serialized data"""
    class Meta:
        model = DateFieldVal
        fields = '__all__'


class NumberFieldSerializer(serializers.ModelSerializer):
    """ Return NumberFieldVal model serialized data"""
    class Meta:
        model = NumberFieldVal
        fields = '__all__'


class RiskFieldSerializer(serializers.ModelSerializer):
    """ Return RiskField model serialized data"""
    number_field = NumberFieldSerializer(many=True, read_only=True)
    enum_field = EnumFieldSerializer(many=True, read_only=True)
    text_field = TextFieldSerializer(many=True, read_only=True)
    date_field = DateFieldSerializer(many=True, read_only=True)

    class Meta:
        model = RiskField
        fields = '__all__'

    # def create(self, validated_data):
    #     risks_number_data = validated_data.pop('number_field')
    #     risks_enum_data = validated_data.pop('enum_field')
    #     risks_date_data = validated_data.pop('date_field')
    #     risks_text_data = validated_data.pop('text_field')
    #     risk_field = RiskField.objects.create(**validated_data)
    #
    #     for risk_number_data in risks_number_data:
    #         NumberFieldVal.objects.create(risk_field=risk_field, **risk_number_data)
    #
    #     for risk_text_data in risks_text_data:
    #         TextFieldVal.objects.create(risk_field=risk_field, **risk_text_data)
    #
    #     for risk_date_data in risks_date_data:
    #         DateFieldVal.objects.create(risk_field=risk_field, **risk_date_data)
    #
    #     for risk_enum_data in risks_enum_data:
    #         EnumFieldVal.objects.create(risk_field=risk_field, **risk_enum_data)
    #
    #     return risk_field


class RiskTypeSerializer(serializers.ModelSerializer):
    """ Return RiskType model serialized data"""
    risk_field = RiskFieldSerializer(many=True, read_only=True)

    class Meta:
        model = RiskType
        fields = '__all__'

    # def create(self, validated_data):
    #     risks_field_data = validated_data.pop('risk_field')
    #     risk_type = RiskType.objects.create(**validated_data)
    #     for risk_field_data in risks_field_data:
    #         RiskField.objects.create(risk_type=risk_type, **risk_field_data)
    #     return risk_type


class RiskSerializer(serializers.ModelSerializer):
    """ Return Risk model serialized data"""
    risk_type = RiskTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Risk
        fields = '__all__'

    # def create(self, validated_data):
    #     risks_type_data = validated_data.pop('risks_type')
    #     risks = Risk.objects.create(**validated_data)
    #     for risk_type_data in risks_type_data:
    #         RiskType.objects.create(risk=risks, **risk_type_data)
    #     return risks