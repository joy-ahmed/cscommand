from django.core.management.base import BaseCommand
import csv
from dataentry.models import *


class Command(BaseCommand):
    help = 'Import data from csv to database'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Path to csv file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['path']
        print(file_path)

        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                existing_student = Student.objects.filter(
                    roll_no=row['roll_no']).exists()
                if not existing_student:
                    Student.objects.create(**row)
                else:
                    raise ValueError('Data already exists')

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
