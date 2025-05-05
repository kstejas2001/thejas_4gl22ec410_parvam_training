from django.db import models

# Create your models here.
class CarParking(models.Model):
    car_brand = models.CharField(max_length=100)
    car_number = models.CharField(max_length=20, unique=True)
    car_type = models.CharField(max_length=20)
    incoming_time = models.DateTimeField(auto_now_add=True)
    outgoing_time = models.DateTimeField(null=True, blank=True)
    parking_slot = models.CharField(max_length=10, unique=True)

    def __str__(self):
       return f"{self.car_number} - {self.parking_slot}"