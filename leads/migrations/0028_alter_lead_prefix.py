# Generated by Django 5.0.2 on 2024-04-03 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0027_lead_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='prefix',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
