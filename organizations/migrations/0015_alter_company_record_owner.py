# Generated by Django 5.0.2 on 2024-03-27 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_rename_modified_crmuser_updated'),
        ('organizations', '0014_company_record_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='record_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.crmuser'),
        ),
    ]
