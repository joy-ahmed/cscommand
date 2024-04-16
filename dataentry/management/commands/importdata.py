from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
import csv

from django.db import DataError

# from dataentry.models import *


class Command(BaseCommand):
    help = 'Import data from csv to database'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Path to csv file')
        parser.add_argument('model', type=str, help='Model name')

    def handle(self, *args, **kwargs):
        file_path = kwargs['path']
        model_name = kwargs['model']

        # model = globals()[model_name]
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = app_config.get_model(model_name)
                break
            except LookupError:
                continue
        if not model:
            raise CommandError(f"Model '{model_name}' not found")

        model_fields = [
            field.name for field in model._meta.fields if field.name != 'id']

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            csv_header = reader.fieldnames
            # compare csv header with model fields
            if csv_header != model_fields:
                raise DataError('CSV header does not match model fields')

            for row in reader:
                existing_data = model.objects.filter(**row).exists()
                if not existing_data:
                    model.objects.create(**row)
                else:
                    raise ValueError('Data already exists')

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
