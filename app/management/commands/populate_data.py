import json
from django.core.management.base import BaseCommand
from app.models import Service

class Command(BaseCommand):
    help = 'Populate the database with data from a JSON file'

    def handle(self, *args, **options):
        json_file_path = 'app/management/commands/population.json'

        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                service = Service(
                    name=item['fields']['name'],
                    description=item['fields']['description'],
                    price=item['fields']['price']
                )
                service.save()

        self.stdout.write(self.style.SUCCESS('Data successfully loaded'))
