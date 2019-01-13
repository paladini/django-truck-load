from django.test import TestCase
from ..models import Truck

class TruckTest(TestCase):
    """ Test module for Truck model """

    def setUp(self):
        Truck.objects.create(
            id_truck=1, truck='Hartford Plastics Incartford', city='Florence', state='AL', lat=34.79981, lng=-87.677251)
        Truck.objects.create(
            id_truck=2, truck='Beyond Landscape & Design Llcilsonville', city='Freemont', state='CA', lat=37.5482697, lng=-121.9885719)

    def test_truck_name(self):
        truck1 = Truck.objects.get(truck='Hartford Plastics Incartford')
        truck2 = Truck.objects.get(truck='Beyond Landscape & Design Llcilsonville')
        self.assertEqual(
            truck1.get_truck_info(), "Hartford Plastics Incartford is located in Florence / AL at latitude 34.799810 and longitude -87.677251")
        self.assertEqual(
            truck2.get_truck_info(), "Beyond Landscape & Design Llcilsonville is located in Freemont / CA at latitude 37.548270 and longitude -121.988572")
