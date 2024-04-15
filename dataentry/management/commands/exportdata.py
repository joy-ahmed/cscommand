from django.core.management.base import BaseCommand
import csv
import os
import datetime
from dataentry.models import *


class Command(BaseCommand):
    help = 'Export data from database to csv'

    def handle(self, *args, **kwargs):
        # fetch data from database
        students = Student.objects.all()

        # define the csv file name/path
        file_name = f"export-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.csv"
        file_path = os.path.join(os.getcwd(), file_name)
        print(file_path)

        # open the csv file and write
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            # write header
            writer.writerow(['Roll No', 'Name', 'Age'])

            # write data rows
            for student in students:
                writer.writerow([student.roll_no, student.name, student.age])

        self.stdout.write(self.style.SUCCESS('Data exported successfully'))
