# Generated by Django 5.0.2 on 2024-04-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capture_form', '0002_district_program_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]