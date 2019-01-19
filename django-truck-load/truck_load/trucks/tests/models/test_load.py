from django.test import TestCase
from ...models import Load

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