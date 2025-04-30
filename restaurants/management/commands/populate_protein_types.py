from django.core.management.base import BaseCommand
from restaurants.models import ProteinType
from restaurants.constants import PROTEIN_TYPE_CHOICES

class Command(BaseCommand):
    help = "Populate ProteinType table with predefined types"

    def handle(self, *args, **kwargs):
        for value, label in PROTEIN_TYPE_CHOICES:
            obj, is_created = ProteinType.objects.get_or_create(name=value)
            if is_created:
                self.stdout.write(self.style.SUCCESS(f"Added {obj}"))
            else:
                self.stdout.write(self.style.WARNING(f"Skipped: {label}"))