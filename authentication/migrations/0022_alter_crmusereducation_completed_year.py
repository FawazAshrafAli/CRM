# Generated by Django 5.0.2 on 2024-04-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0021_crmuserfamilyinformation_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crmusereducation',
            name='completed_year',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
