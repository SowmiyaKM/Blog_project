from django.db import migrations

def create_admin(apps, schema_editor):
    User = apps.get_model("auth", "User")
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="admin123"
        )

class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0011_auto_20251218_1035'),  # <-- last Blog migration
        ('auth', '0012_alter_user_first_name_max_length'),  # keep auth dependency
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]
