# Generated by Django 4.2.6 on 2023-10-20 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0007_alter_maintenance_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='Vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='fleet.vehicle'),
        ),
    ]
