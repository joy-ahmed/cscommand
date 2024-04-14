from django.core.management.base import BaseCommand
import csv
from dataentry.models import *


class Command(BaseCommand):
    help = 'Import data from csv to database'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Path to csv file')
        parser.add_argument('model', type=str, help='Model name')

    def handle(self, *args, **kwargs):
        file_path = kwargs['path']
        model_name = kwargs['model']

        model = globals()[model_name]
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_data = model.objects.filter(**row).exists()
                if not existing_data:
                    model.objects.create(**row)
                else:
                    raise ValueError('Data already exists')

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
