from django.core.management.base import BaseCommand
from Blog.models import Category

class Command(BaseCommand):
    help = "This command inserts category data"

    def handle(self, *args, **kwargs):
        # Deleting the existing data
        Category.objects.all().delete()

        categories = ['Sports', 'Technology', 'Science', 'Art', 'Food']

        for category_name in categories:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting data!"))
