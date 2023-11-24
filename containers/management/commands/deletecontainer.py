from typing import Any
from django.core.management.base import BaseCommand, CommandError
from containers.models import Container

class Command(BaseCommand):
    help = "Last created container in database"

    def handle(self, *args, **options):
        try:
            container = Container.objects.latest('id')
        except:
            raise CommandError('No containers in the database')
        container.delete()

        self.stdout.write(self.style.SUCCESS('Successfully deleted last container'))