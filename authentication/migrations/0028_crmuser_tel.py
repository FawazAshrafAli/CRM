# Generated by Django 5.0.2 on 2024-04-16 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0027_alter_crmuser_reports_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='crmuser',
            name='tel',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True),
        ),
    ]
