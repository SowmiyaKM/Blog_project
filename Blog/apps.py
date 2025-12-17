from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'Blog'

from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Blog"

    def ready(self):
        from django.contrib.auth.models import User
        from django.db.utils import OperationalError

        try:
            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    username="admin",
                    email="admin@example.com",
                    password="admin123"
                )
        except OperationalError:
            pass
