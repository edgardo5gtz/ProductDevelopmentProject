from rest_framework import serializers
from ..Risks.models import *


class RiskSerializer(serializers.ModelSerializer):
    """ Return Risk model serialized data"""
    class Meta:
        model = Risk
        fields = '__all__'


class RiskTypeSerializer(serializers.ModelSerializer):
    """ Return RiskType model serialized data"""
    class Meta:
        model = RiskType
        fields = '__all__'


class RiskFieldSerializer(serializers.ModelSerializer):
    """ Return RiskField model serialized data"""
    class Meta:
        model = RiskField
        fields = '__all__'


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

