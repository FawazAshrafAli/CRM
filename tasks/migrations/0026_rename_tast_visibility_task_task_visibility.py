# Generated by Django 5.0.2 on 2024-04-09 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0025_rename_permission_task_tast_visibility'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tast_visibility',
            new_name='task_visibility',
        ),
    ]
