# import json
# import copy
# from rest_framework import status
# from django.test import TestCase, Client
# from django.urls import reverse
# from ..models import Truck
# from ..models import Load
# from ..serializers import TruckSerializer
# from ..serializers import LoadSerializer


# # initialize the APIClient app
# client = Client()

# class GetAllTrucksTest(TestCase):
#     """ Test module for GET all trucks API """

#     def setUp(self):
#         Truck.objects.create(
#             truck='Hartford Plastics Incartford', 
#             city='Florence', 
#             state='AL', 
#             lat=34.79981, 
#             lng=-87.677251
#         )
#         Truck.objects.create(
#             truck='Beyond Landscape & Design Llcilsonville', 
#             city='Fremont', 
#             state='CA', 
#             lat=37.5482697, 
#             lng=-121.9885719
#         )
#         Truck.objects.create(
#             truck='Empire Of Dirt Llcquality', 
#             city='Hampden', 
#             state='ME', 
#             lat=44.7445421, 
#             lng=-68.8370436
#         )
#         Truck.objects.create(
#             truck='James Haas Al Haas Shelly Haasairfield', 
#             city='North East', 
#             state='MD', 
#             lat=39.6001132, 
#             lng=-75.94133269999999
#         )

#     def test_get_all_trucks(self):
#         # get API response
#         response = client.get(reverse('get_post_trucks'))
#         # get data from db
#         objs = Truck.objects.all()
#         serializer = TruckSerializer(objs, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

# class GetAllLoadsTest(TestCase):
#     """ Test module for GET all loads API """

#     def setUp(self):
#         Load.objects.create(
#             product='Light bulbs', 
#             orig_city='Sikeston', 
#             orig_state='MO',
#             orig_lat=36.876719,
#             orig_lng=-89.5878579,
#             dest_city='Grapevine',
#             dest_state='TX',
#             dest_lat=32.9342919,
#             dest_lng=-97.0780654
#         )
#         Load.objects.create(
#             product='Recyclables', 
#             orig_city='Christiansburg', 
#             orig_state='VA',
#             orig_lat=37.1298517,
#             orig_lng=-80.4089389,
#             dest_city='Apopka',
#             dest_state='FL',
#             dest_lat=28.6934076,
#             dest_lng=-81.5322149
#         )
#         Load.objects.create(
#             product='Apples', 
#             orig_city='Columbus', 
#             orig_state='OH',
#             orig_lat=39.9611755,
#             orig_lng=-82.99879419999999,
#             dest_city='Woodland',
#             dest_state='CA',
#             dest_lat=38.67851570000001,
#             dest_lng=-121.7732971
#         )
#         Load.objects.create(
#             product='Wood', 
#             orig_city='Hebron', 
#             orig_state='KY',
#             orig_lat=39.0661472,
#             orig_lng=-84.70318879999999,
#             dest_city='Jefferson',
#             dest_state='LA',
#             dest_lat=29.96603709999999,
#             dest_lng=-90.1531298
#         )

#     def test_get_all_loads(self):
#         # get API response
#         response = client.get(reverse('get_post_loads'))
#         # get data from db
#         objs = Load.objects.all()
#         serializer = LoadSerializer(objs, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

# class GetSingleTruckTest(TestCase):
#     """ Test module for GET single truck API """

#     def setUp(self):
#         self.obj1 = Truck.objects.create(
#             truck='Hartford Plastics Incartford', 
#             city='Florence', 
#             state='AL', 
#             lat=34.79981, 
#             lng=-87.677251
#         )
#         self.obj2 = Truck.objects.create(
#             truck='Beyond Landscape & Design Llcilsonville', 
#             city='Fremont', 
#             state='CA', 
#             lat=37.5482697, 
#             lng=-121.9885719
#         )
#         self.obj3 = Truck.objects.create(
#             truck='Empire Of Dirt Llcquality', 
#             city='Hampden', 
#             state='ME', 
#             lat=44.7445421, 
#             lng=-68.8370436
#         )
#         self.obj4 = Truck.objects.create(
#             truck='James Haas Al Haas Shelly Haasairfield', 
#             city='North East', 
#             state='MD', 
#             lat=39.6001132, 
#             lng=-75.94133269999999
#         )

#     def test_get_valid_single_truck(self):
#         response = client.get(
#             reverse('get_delete_update_truck', kwargs={'pk': self.obj1.pk}))
#         obj = Truck.objects.get(pk=self.obj1.pk)
#         serializer = TruckSerializer(obj)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_get_invalid_single_truck(self):
#         response = client.get(
#             reverse('get_delete_update_truck', kwargs={'pk': 30}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# class GetSingleLoadTest(TestCase):
#     """ Test module for GET single load API """

#     def setUp(self):
#         self.obj1 = Load.objects.create(
#             product='Light bulbs', 
#             orig_city='Sikeston', 
#             orig_state='MO',
#             orig_lat=36.876719,
#             orig_lng=-89.5878579,
#             dest_city='Grapevine',
#             dest_state='TX',
#             dest_lat=32.9342919,
#             dest_lng=-97.0780654
#         )
#         self.obj2 = Load.objects.create(
#             product='Recyclables', 
#             orig_city='Christiansburg', 
#             orig_state='VA',
#             orig_lat=37.1298517,
#             orig_lng=-80.4089389,
#             dest_city='Apopka',
#             dest_state='FL',
#             dest_lat=28.6934076,
#             dest_lng=-81.5322149
#         )
#         self.obj3 = Load.objects.create(
#             product='Apples', 
#             orig_city='Columbus', 
#             orig_state='OH',
#             orig_lat=39.9611755,
#             orig_lng=-82.99879419999999,
#             dest_city='Woodland',
#             dest_state='CA',
#             dest_lat=38.67851570000001,
#             dest_lng=-121.7732971
#         )
#         self.obj4 = Load.objects.create(
#             product='Wood', 
#             orig_city='Hebron', 
#             orig_state='KY',
#             orig_lat=39.0661472,
#             orig_lng=-84.70318879999999,
#             dest_city='Jefferson',
#             dest_state='LA',
#             dest_lat=29.96603709999999,
#             dest_lng=-90.1531298
#         )

#     def test_get_valid_single_load(self):
#         response = client.get(
#             reverse('get_delete_update_load', kwargs={'pk': self.obj1.pk}))
#         obj = Load.objects.get(pk=self.obj1.pk)
#         serializer = LoadSerializer(obj)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_get_invalid_single_load(self):
#         response = client.get(
#             reverse('get_delete_update_load', kwargs={'pk': 30}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# class CreateNewTruckTest(TestCase):
#     """ Test module for inserting a new truck """

#     def setUp(self):
#         self.valid_payload = {
#             'truck': 'Hartford Plastics Incartford', 
#             'city': 'Florence', 
#             'state': 'AL', 
#             'lat': 34.79981, 
#             'lng': -87.677251
#         }

#     def test_create_valid_truck(self):
#         response = client.post(
#             reverse('get_post_trucks'),
#             data=json.dumps(self.valid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_create_invalid_truck_name(self):
#         invalid = copy.deepcopy(self.valid_payload)
#         invalid['truck'] = ''
#         response = client.post(
#             reverse('get_post_trucks'),
#             data=json.dumps(invalid),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_invalid_truck_city(self):
#         invalid = copy.deepcopy(self.valid_payload)
#         invalid['city'] = ''
#         response = client.post(
#             reverse('get_post_trucks'),
#             data=json.dumps(invalid),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_invalid_truck_state(self):
#         invalid = copy.deepcopy(self.valid_payload)
#         invalid['state'] = ''
#         response = client.post(
#             reverse('get_post_trucks'),
#             data=json.dumps(invalid),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_invalid_truck_lat(self):
#         invalid = copy.deepcopy(self.valid_payload)
#         invalid['lat'] = ''
#         response = client.post(
#             reverse('get_post_trucks'),
#             data=json.dumps(invalid),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_invalid_truck_lng(self):
#         invalid = copy.deepcopy(self.valid_payload)
#         invalid['lng'] = ''        
#         response = client.post(
#             reverse('get_post_trucks'),
#             data=json.dumps(invalid),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# class CreateNewLoad(TestCase):
#     """ Test module for inserting a new load """

#     def setUp(self):
#         self.valid_payload = {
#             'product': 'Light bulbs', 
#             'orig_city': 'Sikeston', 
#             'orig_state': 'MO',
#             'orig_lat': 36.876719,
#             'orig_lng': -89.5878579,
#             'dest_city': 'Grapevine',
#             'dest_state': 'TX',
#             'dest_lat': 32.9342919,
#             'dest_lng': -97.0780654
#         }

#     def test_create_valid_load(self):
#         response = client.post(
#             reverse('get_post_loads'),
#             data=json.dumps(self.valid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_create_invalid_load_name(self):
#         invalid = copy.deepcopy(self.valid_payload)
#         invalid['product'] = ''
#         response = client.post(
#             reverse('get_post_loads'),
#             data=json.dumps(invalid),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_invalid_load_origin_city(self):
#         invalid = copy.deepcopy(self.valid_payload)
#         invalid['orig_city'] = ''
#         response = client.post(
#             reverse('get_post_loads'),
#             data=json.dumps(invalid),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_invalid_load_origin_state(self):
#         invalid = copy.deepcopy(self.valid_payload)
#         invalid['orig_state'] = ''
#         response = client.post(
#             reverse('get_post_loads'),
#             data=json.dumps(invalid),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_invalid_load_origin_lat(self):
#         invalid = copy.deepcopy(self.valid_payload)
#         invalid['orig_lat'] = ''
#         response = client.post(
#             reverse('get_post_loads'),
#             data=json.dumps(invalid),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_invalid_load_origin_lng(self):
#         invalid = copy.deepcopy(self.valid_payload)
#         invalid['orig_lng'] = ''        
#         response = client.post(
#             reverse('get_post_loads'),
#             data=json.dumps(invalid),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_invalid_load_dest_city(self):
#         invalid = copy.deepcopy(self.valid_payload)
#         invalid['dest_city'] = ''
#         response = client.post(
#             reverse('get_post_loads'),
#             data=json.dumps(invalid),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_invalid_load_dest_state(self):
#         invalid = copy.deepcopy(self.valid_payload)
#         invalid['dest_state'] = ''
#         response = client.post(
#             reverse('get_post_loads'),
#             data=json.dumps(invalid),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_invalid_load_dest_lat(self):
#         invalid = copy.deepcopy(self.valid_payload)
#         invalid['dest_lat'] = ''
#         response = client.post(
#             reverse('get_post_loads'),
#             data=json.dumps(invalid),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_invalid_load_dest_lng(self):
#         invalid = copy.deepcopy(self.valid_payload)
#         invalid['dest_lng'] = ''        
#         response = client.post(
#             reverse('get_post_loads'),
#             data=json.dumps(invalid),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# class UpdateSingleTruckTest(TestCase):
#     """ Test module for updating an existing truck record """

#     def setUp(self):
#         self.obj1 = Truck.objects.create(
#             truck='Beyond Landscape & Design Llcilsonville', 
#             city='Fremont', 
#             state='CA', 
#             lat=37.5482697, 
#             lng=-121.9885719
#         )
#         self.valid_payload = { 
#             'truck': 'Beyond Landscape & Design Llcilsonville', 
#             'city': 'test', 
#             'state': 'CA', 
#             'lat': 37.5482697, 
#             'lng': -121.9885719
#         }
#         self.invalid_payload = {
#             'truck': '', 
#             'city': 'Fremont', 
#             'state': 'CA', 
#             'lat': 37.5482697, 
#             'lng': -121.9885719
#         }

#     def test_valid_update_truck(self):
#         response = client.put(
#             reverse('get_delete_update_truck', kwargs={'pk': self.obj1.pk}),
#             data=json.dumps(self.valid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     def test_invalid_update_truck(self):
#         response = client.put(
#             reverse('get_delete_update_truck', kwargs={'pk': self.obj1.pk}),
#             data=json.dumps(self.invalid_payload),
#             content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# class UpdateSingleLoadTest(TestCase):
#     """ Test module for updating an existing load record """

#     def setUp(self):
#         self.obj1 = Load.objects.create(
#             product='Light bulbs', 
#             orig_city='Sikeston', 
#             orig_state='MO',
#             orig_lat=36.876719,
#             orig_lng=-89.5878579,
#             dest_city='Grapevine',
#             dest_state='TX',
#             dest_lat=32.9342919,
#             dest_lng=-97.0780654
#         )
#         self.valid_payload = {
#             'product': 'Light bulbs', 
#             'orig_city': 'Sikeston', 
#             'orig_state': 'AL',
#             'orig_lat': 36.876719,
#             'orig_lng': -89.5878579,
#             'dest_city': 'Grapevine',
#             'dest_state': 'TX',
#             'dest_lat': 32.9342919,
#             'dest_lng': -97.0780654
#         }
#         self.invalid_payload = {
#             'product': 'Light bulbs', 
#             'orig_city': 'Sikeston', 
#             'orig_state': '',
#             'orig_lat': 36.876719,
#             'orig_lng': -89.5878579,
#             'dest_city': 'Grapevine',
#             'dest_state': 'TX',
#             'dest_lat': 32.9342919,
#             'dest_lng': -97.0780654
#         }

#     def test_valid_update_truck(self):
#         response = client.put(
#             reverse('get_delete_update_load', kwargs={'pk': self.obj1.pk}),
#             data=json.dumps(self.valid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     def test_invalid_update_truck(self):
#         response = client.put(
#             reverse('get_delete_update_load', kwargs={'pk': self.obj1.pk}),
#             data=json.dumps(self.invalid_payload),
#             content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# class DeleteSingleTruckTest(TestCase):
#     """ Test module for deleting an existing truck record """

#     def setUp(self):
#         self.obj1 = Truck.objects.create(
#             truck='Beyond Landscape & Design Llcilsonville', 
#             city='Fremont', 
#             state='CA', 
#             lat=37.5482697, 
#             lng=-121.9885719
#         )

#     def test_valid_delete_truck(self):
#         response = client.delete(
#             reverse('get_delete_update_truck', kwargs={'pk': self.obj1.pk}))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     def test_invalid_delete_truck(self):
#         response = client.delete(
#             reverse('get_delete_update_truck', kwargs={'pk': 30}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# class DeleteSingleLoadTest(TestCase):
#     """ Test module for deleting an existing load record """

#     def setUp(self):
#         self.obj1 = Load.objects.create(
#             product='Light bulbs', 
#             orig_city='Sikeston', 
#             orig_state='MO',
#             orig_lat=36.876719,
#             orig_lng=-89.5878579,
#             dest_city='Grapevine',
#             dest_state='TX',
#             dest_lat=32.9342919,
#             dest_lng=-97.0780654
#         )

#     def test_valid_delete_load(self):
#         response = client.delete(
#             reverse('get_delete_update_load', kwargs={'pk': self.obj1.pk}))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     def test_invalid_delete_load(self):
#         response = client.delete(
#             reverse('get_delete_update_load', kwargs={'pk': 30}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
