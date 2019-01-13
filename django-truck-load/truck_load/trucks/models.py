from django.db import models

# Create your models here.
class Truck(models.Model):
    """
    Truck Model
    Define the attributes of a truck
    """
    truck = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_truck_info(self):
        return self.truck + ' is located in ' + self.city + ' / ' + self.state + ' at latitude ' + self.lat + ' and longitude ' + self.lng

    def __repr__(self):
        return self.name + ' is added.'

class Load(models.Model):
    """
    Load Model
    Define the attributes of a load
    """
    product = models.CharField(max_length=255)
    
    # Origin address
    orig_city = models.CharField(max_length=255)
    orig_state = models.CharField(max_length=2)
    orig_lat = models.DecimalField(max_digits=9, decimal_places=6)
    orig_lng = models.DecimalField(max_digits=9, decimal_places=6)
    
    # Destination Adress
    dest_city = models.CharField(max_length=255)
    dest_state = models.CharField(max_length=2)
    dest_lat = models.DecimalField(max_digits=9, decimal_places=6)
    dest_lng = models.DecimalField(max_digits=9, decimal_places=6)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_load_info(self):
        return self.product + ' is located in ' + self.orig_city + ' / ' + self.orig_state + ' and should travel to ' + self.dest_city + ' / ' + self.dest_state + '.'

    def __repr__(self):
        return self.name + ' is added.'