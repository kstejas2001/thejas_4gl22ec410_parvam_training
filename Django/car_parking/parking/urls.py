from django.urls import path
from .views import CarParkingListCreate, CarParkingDetailUpdateDelete

urlpatterns = [
  path('parking/', CarParkingListCreate.as_view(), name='car_parking_list_create'),
  path('parking/<int:pk>/', CarParkingDetailUpdateDelete.as_view(), name='car_parking_detail_update_delete'),
]