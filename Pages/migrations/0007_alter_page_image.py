# Generated by Django 4.2.5 on 2023-10-23 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0006_alter_page_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
