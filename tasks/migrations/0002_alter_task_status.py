# Generated by Django 5.0.2 on 2024-02-27 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Started', 'Started'), ('Not Started', 'Not Started')], max_length=150),
        ),
    ]
