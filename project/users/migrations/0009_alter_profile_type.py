# Generated by Django 4.0.2 on 2022-06-07 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_active_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.type'),
        ),
    ]
