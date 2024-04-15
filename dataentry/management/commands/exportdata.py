from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv
import os
import datetime
from dataentry.models import *


class Command(BaseCommand):
    help = 'Export data from database to csv'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model name')

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name']

        model = None
        # loop through all the models based on argument
        for app_config in apps.get_app_configs():
            try:
                model = app_config.get_model(model_name)
                break
            except LookupError:
                continue

        if not model:
            raise CommandError(f"Model '{model_name}' not found")

         # fetch data from database
        data = model.objects.all()

        # define the csv file name/path
        file_name = f"export-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.csv"
        file_path = os.path.join(os.getcwd(), file_name)
        print(file_path)

        # open the csv file and write
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            # write header
            writer.writerow([field.name for field in model._meta.fields])

            # write data rows
            for record in data:
                writer.writerow([getattr(record, field.name)
                                for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS('Data exported successfully'))
