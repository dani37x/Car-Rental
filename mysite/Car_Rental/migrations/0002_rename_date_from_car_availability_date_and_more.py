# Generated by Django 4.1.1 on 2022-10-02 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Car_Rental', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car_availability',
            old_name='date_from',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='car_availability',
            name='date_to',
        ),
        migrations.RemoveField(
            model_name='car_availability',
            name='price',
        ),
    ]