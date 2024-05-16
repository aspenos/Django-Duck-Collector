from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Duck, Feeding, Pond
from .serializers import DuckSerializer, FeedingSerializer, PondSerializer

# Create your views here.

class DuckList(generics.ListCreateAPIView):
    queryset = Duck.objects.all()
    serializer_class = DuckSerializer

class DuckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Duck.objects.all()
    serializer_class = DuckSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        ponds_not_associated = Pond.objects.exclude(id__in=instance.ponds.all())
        ponds_serializer = PondSerializer(ponds_not_associated, many=True)

        return Response({
            'duck': serializer.data,
            'ponds_not_associated': ponds_serializer.data
        })

class FeedingListCreate(generics.ListCreateAPIView):
    serializer_class = FeedingSerializer

    def get_queryset(self):
        duck_id = self.kwargs['duck_id']
        return Feeding.objects.filter(duck_id=duck_id)

    def perform_create(self, serializer):
        duck_id = self.kwargs['duck_id']
        duck = Duck.objects.get(id=duck_id)
        serializer.save(duck=duck)

class FeedingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeedingSerializer
    lookup_field = 'id'

    def get_queryset(self):
        duck_id = self.kwargs['duck_id']
        return Feeding.objects.filter(duck_id=duck_id)
    
class PondList(generics.ListCreateAPIView):
    queryset = Pond.objects.all()
    serializer_class = PondSerializer

class PondDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pond.objects.all()
    serializer_class = PondSerializer
    lookup_field = 'id'

class AddPondToDuck(APIView):
    def post(self, request, duck_id, pond_id):
        duck = Duck.objects.get(id=duck_id)
        pond = Pond.objects.get(id=pond_id)
        duck.ponds.add(pond)
        return Response({'message': f'Pond {pond.name} added to Duck {duck.name}'})