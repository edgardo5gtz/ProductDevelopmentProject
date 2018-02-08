from rest_framework import generics
from ..Risks.models import *
from .serializers import *


class RiskList(generics.ListCreateAPIView):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer


class RiskDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer


class RiskTypeList(generics.ListCreateAPIView):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer


class RiskTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer


class RiskFieldList(generics.ListCreateAPIView):
    queryset = RiskField.objects.all()
    serializer_class = RiskFieldSerializer


class RiskFieldDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = RiskField.objects.all()
    serializer_class = RiskFieldSerializer


class TextFieldList(generics.ListCreateAPIView):
    queryset = TextFieldVal.objects.all()
    serializer_class = TextFieldSerializer


class TextFieldDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = TextFieldVal.objects.all()
    serializer_class = TextFieldSerializer


class NumberFieldList(generics.ListCreateAPIView):
    queryset = NumberFieldVal.objects.all()
    serializer_class = NumberFieldSerializer


class NumberFieldDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = NumberFieldVal.objects.all()
    serializer_class = NumberFieldSerializer


class EnumFieldList(generics.ListCreateAPIView):
    queryset = EnumFieldVal.objects.all()
    serializer_class = EnumFieldSerializer


class EnumFieldDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnumFieldVal.objects.all()
    serializer_class = EnumFieldSerializer


class DateFieldList(generics.ListCreateAPIView):
    queryset = DateFieldVal.objects.all()
    serializer_class = DateFieldSerializer


class DateFieldDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = DateFieldVal.objects.all()
    serializer_class = DateFieldSerializer

