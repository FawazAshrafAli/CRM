# Generated by Django 5.0.2 on 2024-03-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0010_remove_company_billing_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='billing_country',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='company',
            name='shipping_country',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
