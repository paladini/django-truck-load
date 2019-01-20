import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Truck
from .models import Load
from .serializers import TruckSerializer
from .serializers import LoadSerializer
from .utils import distance_between_coordinates

# /truck/:id_truck
@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_truck(request, pk):
    """
        Retrieve/Delete/Update a specific Truck.
    """
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
        truck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # update details of a single truck
    elif request.method == 'PUT':
        serializer = TruckSerializer(truck, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /trucks
@api_view(['GET', 'POST'])
def get_post_trucks(request):
    """
        Retrieve all Trucks from database or insert a new Truck record.
    """
    # get all trucks
    if request.method == 'GET':
        trucks = Truck.objects.all()
        serializer = TruckSerializer(trucks, many=True)
        return Response(serializer.data)

    # insert a new record for a truck
    elif request.method == 'POST':
        data = {
            'truck': request.data.get('truck'),
            'city': request.data.get('city'),
            'state': request.data.get('state'),
            'lat': request.data.get('lat'),
            'lng': request.data.get('lng')
        }
        serializer = TruckSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /load/:id_load
@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_load(request, pk):
    """
        Retrieve/Delete/Update a specific Load.
    """
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
        load.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # update details of a single load
    elif request.method == 'PUT':
        serializer = LoadSerializer(load, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /loads
@api_view(['GET', 'POST'])
def get_post_loads(request):
    """
        Retrieve all Loads from database or insert a new Load record.
    """
    # get all loads
    if request.method == 'GET':
        loads = Load.objects.all()
        serializer = LoadSerializer(loads, many=True)
        return Response(serializer.data)

    # insert a new record for a load
    elif request.method == 'POST':
        data = {
            'product': request.data.get('product'), 
            'orig_city': request.data.get('orig_city'), 
            'orig_state': request.data.get('orig_state'),
            'orig_lat': request.data.get('orig_lat'),
            'orig_lng': request.data.get('orig_lng'),
            'dest_city': request.data.get('dest_city'),
            'dest_state': request.data.get('dest_state'),
            'dest_lat': request.data.get('dest_lat'),
            'dest_lng': request.data.get('dest_lng')
        }
        serializer = LoadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /map_trucks_to_loads
@api_view(['GET'])
def get_map_trucks_to_loads(request):
    """
        Retrieve all trucks and loads, calculate the best route for each truck transport the loads and returns it in a JSON format.
    """

    if request.method == 'GET':

        # structure = {
        #     <load_id>: [
        #         <distance_in_km>: <truck_id>,
        #         <distance_in_km>: <truck_id>,
        #         ...
        #     ]
        # }

        loads = Load.objects.all()
        loadSerializer = LoadSerializer(loads, many=True)

        trucks = Truck.objects.all()
        truckSerializer = TruckSerializer(trucks, many=True)

        # If there's no cargos, return an error
        if (len(loads) <= 0):
            return Response({'message': 'No cargos found in the database.'}, status=status.HTTP_400_BAD_REQUEST)

        # If there's no trucks, return an error
        if (len(trucks) <= 0):
            return Response({'message': 'No trucks found in the database.'}, status=status.HTTP_400_BAD_REQUEST)

        def sort_by_distance(e):
            return e['distance']

        # Calculates the distance between trucks and all the loads/cargos.
        distances = {}
        for load in loads:

            # Calculates the distance between the origin of a specific load/cargo and all the available trucks
            load_distances = []
            # load_distances = {}
            for truck in trucks:
                # load_distances[distance_between_coordinates(truck.lat, truck.lng, load.orig_lat, load.orig_lng)] = truck.pk
                load_distances.append({
                    "distance": distance_between_coordinates(truck.lat, truck.lng, load.orig_lat, load.orig_lng),
                    "truck_id": truck.pk
                })
                # load_distances[] = truck.pk

            load_distances = sorted(load_distances, key=lambda d: float(d['distance']))
            # load_distances = load_distances.sort(key=sort_by_distance)
            print(load_distances)
            distances[load.pk] = load_distances[:2]

        # Find the best route for each load
        # print(distances)

        best_route = {}
        for load in distances.keys():

            # best_routes_for_load = [distances[load_id].keys()]
            best_routes_for_load = []

            # print(distances[load])


            # while (len(best_routes_for_load) < 3):
            #     min_route = min(distances[load_id], key=distances[load_id].get)
            #     best_routes_for_load.append(min_route)
            #     del distances[load_id][min_route]

            # print("\n\n---------------\n")
            # print("All routes: ")
            # print(list(distances[load_id].keys()))
            # print("\nBest routes: ")
            # print(best_routes_for_load)
            # print(best_routes_for_load)
            # for truck_distance in distances[load_id].items():


            #     best_routes_for_load[truck_distance] = 

            # best_route[load_id] = min(distances[load_id], key=distances[load_id].get)

        return Response(best_route)

