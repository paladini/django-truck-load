from django.core.management.base import BaseCommand, CommandError
from trucks.models import Truck
import csv

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.DictReader(open(csv_file), delimiter=',', quotechar='"')

            for row in dataReader:

                truck = Truck.objects.create(
                    truck=row['truck'], 
                    city=row['city'], 
                    state=row['state'], 
                    lat=row['lat'], 
                    lng=row['lng']
                )
                self.stdout.write(
                    'Created truck {} that is located in {} / {}'.format(truck.truck, truck.city, truck.state)
                )