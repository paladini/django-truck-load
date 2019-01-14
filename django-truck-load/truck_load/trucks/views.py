from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Truck
from .models import Load
from .serializers import TruckSerializer
from .serializers import LoadSerializer

# /truck/:id_truck
@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_truck(request, pk):
    try:
        truck = Truck.objects.get(pk=pk)
    except Truck.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single truck
    if request.method == 'GET':
        serializer = TruckSerializer(truck)
        return Response(serializer.data)
    # delete a single truck
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single truck
    elif request.method == 'PUT':
        return Response({})

# /trucks
@api_view(['GET', 'POST'])
def get_post_trucks(request):
    # get all trucks
    if request.method == 'GET':
        trucks = Truck.objects.all()
        serializer = TruckSerializer(trucks, many=True)
        return Response(serializer.data)
    # insert a new record for a truck
    elif request.method == 'POST':
        data = {
            'id_truck': request.data.get('id_truck'), 
            'truck': request.data.get('truck'), 
            'city': request.data.get('city'), 
            'state': request.data.get('state'), 
            'lat': float(request.data.get('lat')), 
            'lng': float(request.data.get('lng'))
        }
        serializer = TruckSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /load/:id_load
@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_load(request, pk):
    try:
        load = Load.objects.get(pk=pk)
    except Load.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single load
    if request.method == 'GET':
        serializer = LoadSerializer(load)
        return Response(serializer.data)
    # delete a single load
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single load
    elif request.method == 'PUT':
        return Response({})

# /loads
@api_view(['GET', 'POST'])
def get_post_loads(request):
    # get all loads
    if request.method == 'GET':
        loads = Load.objects.all()
        serializer = LoadSerializer(loads, many=True)
        return Response(serializer.data)
    # insert a new record for a load
    elif request.method == 'POST':

    	
    	
        data = {
        	'id_load': request.data.get('id_load'), 
			'product': request.data.get('product'), 
			'orig_city': request.data.get('orig_city'), 
			'orig_state': request.data.get('orig_state'),
			'orig_lat': float(request.data.get('orig_lat')),
			'orig_lng': float(request.data.get('orig_lng')),
			'dest_city': request.data.get('dest_city'),
			'dest_state': request.data.get('dest_state'),
			'dest_lat': float(request.data.get('dest_lat')),
			'dest_lng': float(request.data.get('dest_lng'))
        }
        serializer = LoadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)