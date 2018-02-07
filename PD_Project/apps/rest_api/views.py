from rest_framework import generics
from ..Risks.models import Risk
from .serializers import RiskSerializer


class RisksList(generics.ListCreateAPIView):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer


class RisksDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer

