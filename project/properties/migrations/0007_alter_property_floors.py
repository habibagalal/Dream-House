# Generated by Django 4.0.2 on 2022-06-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_uploadedprob_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='floors',
            field=models.IntegerField(null=True),
        ),
    ]
