# Generated by Django 4.2.5 on 2023-10-22 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='imagen',
            new_name='image',
        ),
    ]