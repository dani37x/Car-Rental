# Generated by Django 4.1.1 on 2022-10-02 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car_Rental', '0002_rename_date_from_car_availability_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='price',
            field=models.IntegerField(default=100),
        ),
    ]