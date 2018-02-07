from rest_framework import serializers
from ..Risks.models import Risk


class RiskSerializer(serializers.ModelSerializer):
    """ Return risk model serialized data"""
    class Meta:
        model = Risk
        fields = '__all__'

