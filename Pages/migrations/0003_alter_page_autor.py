# Generated by Django 4.2.5 on 2023-10-22 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Pages', '0002_rename_imagen_avatar_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
