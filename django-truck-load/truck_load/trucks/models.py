from django.db import models

# Create your models here.
class Truck(models.Model):
    """
    Truck Model
    Define the attributes of a truck
    """
    id_truck = models.IntegerField(primary_key=True)
    truck = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def clean(self):
        if (not self.id_truck) or (self.id_truck <= 0):
            raise ValidationError("Truck ID must be be greater than 0.")

        if (not self.truck) or (not self.truck.strip()):
            raise ValidationError("Truck name cannot be empty.")

        if (not self.city) or (not self.city.strip()):
            raise ValidationError("City name cannot be empty.")

        if (not self.state) or (not self.state.strip()):
            raise ValidationError("State name cannot be empty and it's size should be only 2 characters.")

        if (not self.lat) or (not self.lat <= 0):
            raise ValidationError("Latitude should be greater than 0.")
        
        if (not self.lng) or (not self.lng <= 0):
            raise ValidationError("Longitude should be greater than 0.")

    def get_truck_info(self):
        return self.truck + ' is located in ' + self.city + ' / ' + self.state + ' at latitude ' + str(self.lat) + ' and longitude ' + str(self.lng)

    def __repr__(self):
        return self.truck + ' is added.'

class Load(models.Model):
    """
    Load Model
    Define the attributes of a load
    """
    id_load = models.IntegerField(primary_key=True)
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
    
    def clean(self):
        if (not self.id_load) or (not self.id_load <= 0):
            raise ValidationError("Load ID should be greater than 0.")

        if (not self.product) or (not self.product.strip()):
            raise ValidationError("Load name cannot be empty.")

        if (not self.orig_city) or (not self.orig_city.strip()):
            raise ValidationError("Origin City name cannot be empty.")

        if (not self.orig_state) or (not self.orig_state.strip()):
            raise ValidationError("Origin State name cannot be empty and it's size should be only 2 characters.")

        if (not self.orig_lat) or (not self.orig_lat <= 0):
            raise ValidationError("Origin Latitude should be greater than 0.")
        
        if (not self.orig_lng) or (not self.orig_lng <= 0):
            raise ValidationError("Origin Longitude should be greater than 0.")

        if (not self.dest_city) or (not self.dest_city.strip()):
            raise ValidationError("Origin City name cannot be empty.")

        if (not self.dest_state) or (not self.dest_state.strip()):
            raise ValidationError("Origin State name cannot be empty and it's size should be only 2 characters.")

        if (not self.dest_lat) or (not self.dest_lat <= 0):
            raise ValidationError("Origin Latitude should be greater than 0.")
        
        if (not self.dest_lng) or (not self.dest_lng <= 0):
            raise ValidationError("Origin Longitude should be greater than 0.")

    def get_load_info(self):
        return self.product + ' is located in ' + self.orig_city + ' / ' + self.orig_state + ' and should travel to ' + self.dest_city + ' / ' + self.dest_state + '.'

    def __repr__(self):
        return self.product + ' is added.'

