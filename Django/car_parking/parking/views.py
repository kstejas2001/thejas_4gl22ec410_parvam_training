from .models import CarParking
from .serializers import CarParkingSerializer
from rest_framework import generics

# Create your views here.
class CarParkingListCreate(generics.ListCreateAPIView):
    queryset = CarParking.objects.all()
    serializer_class = CarParkingSerializer

class CarParkingDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarParking.objects.all()
    serializer_class = CarParkingSerializer