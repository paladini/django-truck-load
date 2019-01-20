from django.core.management.base import BaseCommand, CommandError
from trucks.models import Load
import csv

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.DictReader(open(csv_file), delimiter=',', quotechar='"')

            for row in dataReader:

                load = Load.objects.create(
                    product=row['product'],
                    orig_city=row['origin_city'], 
                    orig_state=row['origin_state'],
                    orig_lat=row['origin_lat'],
                    orig_lng=row['origin_lng'],
                    dest_city=row['destination_city'],
                    dest_state=row['destination_state'],
                    dest_lat=row['destination_lat'],
                    dest_lng=row['destination_lng']
                )
                self.stdout.write(
                    'Created cargo named {}.'.format(load.product)
                )