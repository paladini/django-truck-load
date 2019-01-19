import json
import copy
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ...models import Truck
from ...serializers import TruckSerializer


# initialize the APIClient app
client = Client()

class GetAllTrucksTest(TestCase):
    """ Test module for GET all trucks API """

    def setUp(self):
        Truck.objects.create(
            truck='Hartford Plastics Incartford', 
            city='Florence', 
            state='AL', 
            lat=34.79981, 
            lng=-87.677251
        )
        Truck.objects.create(
            truck='Beyond Landscape & Design Llcilsonville', 
            city='Fremont', 
            state='CA', 
            lat=37.5482697, 
            lng=-121.9885719
        )
        Truck.objects.create(
            truck='Empire Of Dirt Llcquality', 
            city='Hampden', 
            state='ME', 
            lat=44.7445421, 
            lng=-68.8370436
        )
        Truck.objects.create(
            truck='James Haas Al Haas Shelly Haasairfield', 
            city='North East', 
            state='MD', 
            lat=39.6001132, 
            lng=-75.94133269999999
        )

    def test_get_all_trucks(self):
        # get API response
        response = client.get(reverse('get_post_trucks'))
        # get data from db
        objs = Truck.objects.all()
        serializer = TruckSerializer(objs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleTruckTest(TestCase):
    """ Test module for GET single truck API """

    def setUp(self):
        self.obj1 = Truck.objects.create(
            truck='Hartford Plastics Incartford', 
            city='Florence', 
            state='AL', 
            lat=34.79981, 
            lng=-87.677251
        )
        self.obj2 = Truck.objects.create(
            truck='Beyond Landscape & Design Llcilsonville', 
            city='Fremont', 
            state='CA', 
            lat=37.5482697, 
            lng=-121.9885719
        )
        self.obj3 = Truck.objects.create(
            truck='Empire Of Dirt Llcquality', 
            city='Hampden', 
            state='ME', 
            lat=44.7445421, 
            lng=-68.8370436
        )
        self.obj4 = Truck.objects.create(
            truck='James Haas Al Haas Shelly Haasairfield', 
            city='North East', 
            state='MD', 
            lat=39.6001132, 
            lng=-75.94133269999999
        )

    def test_get_valid_single_truck(self):
        response = client.get(
            reverse('get_delete_update_truck', kwargs={'pk': self.obj1.pk}))
        obj = Truck.objects.get(pk=self.obj1.pk)
        serializer = TruckSerializer(obj)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_truck(self):
        response = client.get(
            reverse('get_delete_update_truck', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewTruckTest(TestCase):
    """ Test module for inserting a new truck """

    def setUp(self):
        self.valid_payload = {
            'truck': 'Hartford Plastics Incartford', 
            'city': 'Florence', 
            'state': 'AL', 
            'lat': 34.79981, 
            'lng': -87.677251
        }

    def test_create_valid_truck(self):
        response = client.post(
            reverse('get_post_trucks'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_truck_name(self):
        invalid = copy.deepcopy(self.valid_payload)
        invalid['truck'] = ''
        response = client.post(
            reverse('get_post_trucks'),
            data=json.dumps(invalid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_truck_city(self):
        invalid = copy.deepcopy(self.valid_payload)
        invalid['city'] = ''
        response = client.post(
            reverse('get_post_trucks'),
            data=json.dumps(invalid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_truck_state(self):
        invalid = copy.deepcopy(self.valid_payload)
        invalid['state'] = ''
        response = client.post(
            reverse('get_post_trucks'),
            data=json.dumps(invalid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_truck_lat(self):
        invalid = copy.deepcopy(self.valid_payload)
        invalid['lat'] = ''
        response = client.post(
            reverse('get_post_trucks'),
            data=json.dumps(invalid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_truck_lng(self):
        invalid = copy.deepcopy(self.valid_payload)
        invalid['lng'] = ''        
        response = client.post(
            reverse('get_post_trucks'),
            data=json.dumps(invalid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleTruckTest(TestCase):
    """ Test module for updating an existing truck record """

    def setUp(self):
        self.obj1 = Truck.objects.create(
            truck='Beyond Landscape & Design Llcilsonville', 
            city='Fremont', 
            state='CA', 
            lat=37.5482697, 
            lng=-121.9885719
        )
        self.valid_payload = { 
            'truck': 'Beyond Landscape & Design Llcilsonville', 
            'city': 'test', 
            'state': 'CA', 
            'lat': 37.5482697, 
            'lng': -121.9885719
        }
        self.invalid_payload = {
            'truck': '', 
            'city': 'Fremont', 
            'state': 'CA', 
            'lat': 37.5482697, 
            'lng': -121.9885719
        }

    def test_valid_update_truck(self):
        response = client.put(
            reverse('get_delete_update_truck', kwargs={'pk': self.obj1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_truck(self):
        response = client.put(
            reverse('get_delete_update_truck', kwargs={'pk': self.obj1.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleTruckTest(TestCase):
    """ Test module for deleting an existing truck record """

    def setUp(self):
        self.obj1 = Truck.objects.create(
            truck='Beyond Landscape & Design Llcilsonville', 
            city='Fremont', 
            state='CA', 
            lat=37.5482697, 
            lng=-121.9885719
        )

    def test_valid_delete_truck(self):
        response = client.delete(
            reverse('get_delete_update_truck', kwargs={'pk': self.obj1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_truck(self):
        response = client.delete(
            reverse('get_delete_update_truck', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
