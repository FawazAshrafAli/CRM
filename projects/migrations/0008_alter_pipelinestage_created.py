# Generated by Django 5.0.2 on 2024-03-20 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_pipelinestage_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipelinestage',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
