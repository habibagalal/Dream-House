# Generated by Django 4.0.2 on 2022-06-15 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0032_alter_property_lat_alter_property_long_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.DecimalField(blank=0, decimal_places=7, max_digits=13, null=True),
        ),
    ]
