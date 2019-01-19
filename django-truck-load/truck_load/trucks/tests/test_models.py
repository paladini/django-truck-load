from django.test import TestCase
from ..models import Truck
from ..models import Load

class TruckTest(TestCase):
    """ Test module for Truck model """

    def setUp(self):
        Truck.objects.create(
            truck='Hartford Plastics Incartford', city='Florence', state='AL', lat=34.79981, lng=-87.677251)
        Truck.objects.create(
            truck='Beyond Landscape & Design Llcilsonville', city='Freemont', state='CA', lat=37.5482697, lng=-121.9885719)

    def test_truck_name(self):
        truck1 = Truck.objects.get(truck='Hartford Plastics Incartford')
        truck2 = Truck.objects.get(truck='Beyond Landscape & Design Llcilsonville')
        self.assertEqual(
            truck1.get_truck_info(), "Hartford Plastics Incartford is located in Florence / AL at latitude 34.7998100 and longitude -87.6772510")
        self.assertEqual(
            truck2.get_truck_info(), "Beyond Landscape & Design Llcilsonville is located in Freemont / CA at latitude 37.5482697 and longitude -121.9885719")

class LoadTest(TestCase):
    """ Test module for Load model """

    def setUp(self):
        Load.objects.create(
            product='Light bulbs', 
            orig_city='Sikeston', 
            orig_state='MO',
            orig_lat=36.876719,
            orig_lng=-89.5878579,
            dest_city='Grapevine',
            dest_state='TX',
            dest_lat=32.9342919,
            dest_lng=-97.0780654
        )
        Load.objects.create(
            product='Recyclables', 
            orig_city='Christiansburg', 
            orig_state='VA',
            orig_lat=37.1298517,
            orig_lng=-80.4089389,
            dest_city='Apopka',
            dest_state='FL',
            dest_lat=28.6934076,
            dest_lng=-81.5322149
        )

    def test_load_name(self):
        obj1 = Load.objects.get(product='Light bulbs')
        obj2 = Load.objects.get(product='Recyclables')
        self.assertEqual(
            obj1.get_load_info(), "Light bulbs is located in Sikeston / MO and should travel to Grapevine / TX.")
        self.assertEqual(
            obj2.get_load_info(), "Recyclables is located in Christiansburg / VA and should travel to Apopka / FL.")