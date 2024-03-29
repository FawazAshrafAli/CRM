# Generated by Django 5.0.2 on 2024-03-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='shipping_city',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='shipping_country',
            field=models.CharField(blank=True, default='India', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='shipping_postal_code',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='shipping_state',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
