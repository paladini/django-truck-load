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
        return Response({})
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
        return Response({})

# /load/:id_load
@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_load(request, pk):
    try:
        load = Load.objects.get(pk=pk)
    except Load.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single load
    if request.method == 'GET':
        return Response({})
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
        return Response({})