# Generated by Django 4.0.2 on 2022-06-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0022_alter_property_sqft_living_alter_property_sqft_above_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='lat',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True),
        ),
    ]