# Generated by Django 5.0.2 on 2024-03-14 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0018_alter_lead_lead_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='phone',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
