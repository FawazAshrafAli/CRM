# Generated by Django 5.0.2 on 2024-03-02 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='percentage_completed',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Not Started', 'Not Started'), ('Completed', 'Completed'), ('In Progress', 'In Progress')], max_length=150),
        ),
    ]
