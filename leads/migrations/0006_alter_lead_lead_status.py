# Generated by Django 5.0.2 on 2024-03-05 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_alter_lead_lead_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='lead_status',
            field=models.CharField(default='OPEN - Not Contacted', max_length=150),
        ),
    ]
