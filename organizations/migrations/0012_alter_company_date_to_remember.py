# Generated by Django 5.0.2 on 2024-03-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0011_alter_company_billing_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='date_to_remember',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]