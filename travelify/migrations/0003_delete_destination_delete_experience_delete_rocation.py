# Generated by Django 4.0.4 on 2022-07-30 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelify', '0002_place'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Destination',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='Rocation',
        ),
    ]
