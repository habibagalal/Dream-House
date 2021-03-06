# Generated by Django 4.0.2 on 2022-06-20 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0037_alter_property_bathrooms_alter_property_floors'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={},
        ),
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='PropImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('Property', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
    ]
