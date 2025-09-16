from django.shortcuts import render

from rest_framework import viewsets
from marketPrice.models import Crop, MarketPrice
from .serializers import CropSerializer, MarketPriceSerializer

# Create your views here.

class CropViewset(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class MarketPriceViewset(viewsets.ModelViewSet):
    queryset = MarketPrice.objects.all()
    serializer_class = MarketPriceSerializer
