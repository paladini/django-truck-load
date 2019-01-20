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

        """
        distances_structure = {
            <load_id>: [
                { "distance": <distance_in_km>, "truck_id": <truck_id>},
                { "distance": <distance_in_km>, "truck_id": <truck_id>},
                ...
            ]
        }
        """

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


        # Calculates all the distances between trucks and the loads/cargos.
        distances = {}
        distances_nearest = {}
        assigned_trucks = {}
        for load in loads:

            # Calculates the distance between the origin of a specific load/cargo and all the available trucks
            load_distances = []
            for truck in trucks:
                load_distances.append({
                    "distance": distance_between_coordinates(truck.lat, truck.lng, load.orig_lat, load.orig_lng),
                    "truck_id": truck.pk
                })

            load_distances = sorted(load_distances, key=lambda d: float(d['distance']))
            
            # Stores the distance from all the trucks to this load
            distances[load.pk] = load_distances

            # Stores the distance from the 3 nearest trucks to this load
            distances_nearest[load.pk] = load_distances[:3]

            # Check if the nearest truck is still available
            for near_truck in distances_nearest[load.pk]:

                # If the truck is not assigned to other load, then assign this load to the nearest truck.
                if near_truck["truck_id"] not in assigned_trucks:
                    assigned_trucks[near_truck["truck_id"]] = {
                        "load_id": load.pk,
                        "distance": near_truck["distance"]
                    }
                    break
                else:

                    # Check if the distance between already assigned truck and it's load is lesser than the distance between this truck and the current load being tested.
                    assigned_truck = assigned_trucks[near_truck["truck_id"]]
                    if assigned_truck["distance"] > near_truck["distance"]:

                        # Then checks if the distance (a) between the already assigned load and it's second truck option; is less than the distance (b) between the current load and the already assigned truck
                        # If (a) distance <= (b) distance:
                        #   1. Replaces the already assigned truck for the second option of the already assigned load
                        #   2. Assign the old assigned truck to the current load
                        if distances_nearest[assigned_truck["load_id"]][1]["distance"] <= near_truck["distance"]:
                            
                            # 1.1 - Removes the assigned truck from the already assigned load
                            assigned_load_id = assigned_truck["load_id"]
                            del assigned_trucks[near_truck["truck_id"]]

                            # 1.2 - Assign the "already assigned load" to it's second nearest truck
                            assigned_trucks[distances_nearest[assigned_load_id][1]["truck_id"]] = {
                                "load_id": assigned_load_id,
                                "distance": distances_nearest[assigned_load_id][1]["distance"]
                            }

                            # 2.1 - Assign the old assigned truck to the current load
                            assigned_trucks[near_truck["truck_id"]] = {
                                "load_id": load.pk,
                                "distance": near_truck["distance"]
                            }
                            break


        # Calculates the route overall distance in km
        overall_distance_to_loads = 0.0
        overall_distance_between_origins_and_dests = 0.0
        overall_assigns = []
        for truck_id, assigned_load in assigned_trucks.items():

            current_load = Load.objects.get(pk=assigned_load["load_id"])
            current_truck = Truck.objects.get(pk=truck_id)

            distance_between_orig_and_dest = distance_between_coordinates(current_load.dest_lat, current_load.dest_lng, current_load.orig_lat, current_load.orig_lng)
            overall_distance_between_origins_and_dests += distance_between_orig_and_dest
            overall_distance_to_loads += assigned_load["distance"]

            overall_assigns.append({

                # Load/Cargo related stuff
                "load_id": assigned_load["load_id"], 
                "load_name": current_load.product,
                "load_origin_city": current_load.orig_city,
                "load_origin_state": current_load.orig_state,
                "load_origin_latitude": current_load.orig_lat,
                "load_origin_longitude": current_load.orig_lng,
                "load_destination_city": current_load.dest_city,
                "load_destination_state": current_load.dest_state,
                "load_destination_latitude": current_load.dest_lat,
                "load_destination_longitude": current_load.dest_lng,
                "load_distance_between_origin_and_destination": distance_between_orig_and_dest,

                # Truck related stuff 
                "truck_id": truck_id,
                "truck_name": current_truck.truck,
                "truck_latitude": current_truck.lat,
                "truck_longitude": current_truck.lng,
                "truck_city": current_truck.city,
                "truck_state": current_truck.state,
                "truck_distance_to_load_origin": assigned_load["distance"]
            })

        overall_distance_total = overall_distance_to_loads + overall_distance_between_origins_and_dests
        response = {
            "overall_distance_to_loads": overall_distance_to_loads,
            "overall_distance_between_origins_and_dests": overall_distance_between_origins_and_dests,
            "overall_distance_total": overall_distance_total,
            "unit": "km",
            "assigns": overall_assigns
        }
        return Response(response)

