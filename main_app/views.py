from django.shortcuts import render
from rest_framework import generics
from .models import Duck
from .serializers import DuckSerializer

# Create your views here.

class DuckList(generics.ListCreateAPIView):
    queryset = Duck.objects.all()
    serializer_class = DuckSerializer

class DuckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Duck.objects.all()
    serializer_class = DuckSerializer
    lookup_field = 'id'