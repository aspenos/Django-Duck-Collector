from rest_framework import serializers
from .models import Duck, Feeding, Pond


class PondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pond
        fields = '__all__'

class DuckSerializer(serializers.ModelSerializer):
    ponds = PondSerializer(many=True, read_only=True)
    class Meta:
        model = Duck
        fields = '__all__'
        

class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'
        read_only_fields = ('duck',)


