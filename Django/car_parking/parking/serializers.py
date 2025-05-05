from rest_framework import serializers
from .models import CarParking

class CarParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarParking
        fields = '__all__'