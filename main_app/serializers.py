from rest_framework import serializers
from .models import Duck, Feeding, Pond
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']
      )
      
      return user

class PondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pond
        fields = '__all__'

class DuckSerializer(serializers.ModelSerializer):
    ponds = PondSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Duck
        fields = '__all__'
        

class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'
        read_only_fields = ('duck',)


