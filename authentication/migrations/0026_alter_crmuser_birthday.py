# Generated by Django 5.0.2 on 2024-04-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0025_crmuser_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crmuser',
            name='birthday',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]