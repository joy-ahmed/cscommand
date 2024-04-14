from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    help = "Insert data into database"
    data = [
        {'roll_no': 1, 'name': 'Ramesh', 'age': 25},
        {'roll_no': 2, 'name': 'Suresh', 'age': 45},
        {'roll_no': 3, 'name': 'Ganesh', 'age': 60},
    ]

    def handle(self, *args, **kwargs):
        try:
            for d in self.data:
                exiting_student = Student.objects.filter(
                    roll_no=d['roll_no']).exists()
                if not exiting_student:
                    Student.objects.create(**d)
                else:
                    raise ValueError('Data already exists')

            self.stdout.write(self.style.SUCCESS('Data inserted successfully'))
        except:
            self.stdout.write(self.style.ERROR('Data insertion failed'))
