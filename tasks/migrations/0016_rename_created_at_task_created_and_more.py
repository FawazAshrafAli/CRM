# Generated by Django 5.0.2 on 2024-03-21 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='updated_at',
            new_name='updated',
        ),
    ]
