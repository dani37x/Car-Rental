# Generated by Django 4.1.1 on 2022-10-02 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Car_Rental', '0003_details_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='price',
            new_name='price_for_day',
        ),
    ]