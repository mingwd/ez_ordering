from django.core.management.base import BaseCommand
from restaurants.models import Tag
from restaurants.cons import ALL_TAGS

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        count = 0
        for category, choices in ALL_TAGS:
            for value, label in choices:
                tag, created = Tag.objects.get_or_create(name=label, category=category)
                if created:
                    count += 1
        self.stdout.write(self.style.SUCCESS(f"Created {count} new tags."))