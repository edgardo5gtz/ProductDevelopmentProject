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
        fields = ('value', 'risk_type', 'risk_field')


class RiskFieldSerializer(serializers.ModelSerializer):
    """ Return RiskField model serialized data"""
    number_val_field = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = RiskField
        fields = '__all__'


class RiskTypeSerializer(serializers.ModelSerializer):
    """ Return RiskType model serialized data"""
    number_val_type = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = RiskType
        fields = '__all__'


class RiskSerializer(serializers.ModelSerializer):
    """ Return Risk model serialized data"""
    
    class Meta:
        model = Risk
        fields = '__all__'
