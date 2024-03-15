# Generated by Django 5.0.2 on 2024-03-15 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_crmuser_email_alter_crmuser_passport_number_and_more'),
        ('deals', '0008_alter_deal_actual_close_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='user_responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.crmuser'),
        ),
    ]
