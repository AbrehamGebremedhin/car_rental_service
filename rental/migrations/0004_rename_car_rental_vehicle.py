# Generated by Django 4.2.6 on 2023-10-23 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_alter_rental_car_alter_rental_customer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rental',
            old_name='car',
            new_name='vehicle',
        ),
    ]
