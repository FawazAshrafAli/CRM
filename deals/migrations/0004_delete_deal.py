# Generated by Django 5.0.2 on 2024-03-06 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0003_alter_deal_forecast_close_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Deal',
        ),
    ]
