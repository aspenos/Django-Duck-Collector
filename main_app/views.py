from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Duck, Feeding, Pond
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import DuckSerializer, FeedingSerializer, PondSerializer, UserSerializer

# Create your views here.

class DuckList(generics.ListCreateAPIView):
    queryset = Duck.objects.all()
    serializer_class = DuckSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
      user = self.request.user
      return Duck.objects.filter(user=user)
    
    def perform_create(self, serializer):
      serializer.save(user=self.request.user)

class DuckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Duck.objects.all()
    serializer_class = DuckSerializer
    lookup_field = 'id'

def get_queryset(self):
    user = self.request.user
    return Duck.objects.filter(user=user) 

def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    ponds_not_associated = Pond.objects.exclude(id__in=instance.ponds.all())
    ponds_serializer = PondSerializer(ponds_not_associated, many=True)

    return Response({
      'duck': serializer.data,
      'ponds_not_associated': ponds_serializer.data
    })

def perform_update(self, serializer):
    duck = self.get_object()
    if duck.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to edit this duck."})
    serializer.save()

def perform_destroy(self, instance):
    if instance.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to delete this duck."})
    instance.delete()

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
    
class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })

# User Login
class LoginView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# User Verification
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })