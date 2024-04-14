from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = 'Prints "Greetings"'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Your name')
    
    def handle(self, *args, **kwargs):
        name = kwargs['name']
        self.stdout.write(f'Hello, {name}!')