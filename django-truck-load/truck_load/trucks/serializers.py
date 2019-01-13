from rest_framework import serializers
from .models import Load
from .models import Truck

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ('id_truck', 'truck', 'city', 'state', 'lat', 'lng', 'created_at', 'updated_at')

class LoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Load
        fields = ('id_load', 'product', 'orig_city', 'orig_state', 'orig_lat', 'orig_lng', 'dest_city', 'dest_state', 'dest_lat', 'dest_lng', 'created_at', 'updated_at')