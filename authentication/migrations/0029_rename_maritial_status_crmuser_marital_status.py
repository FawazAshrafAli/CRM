# Generated by Django 5.0.2 on 2024-04-16 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0028_crmuser_tel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crmuser',
            old_name='maritial_status',
            new_name='marital_status',
        ),
    ]
