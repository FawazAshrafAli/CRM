# Generated by Django 5.0.2 on 2024-03-11 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0011_delete_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('assigned_to', models.CharField(blank=True, default='Me', max_length=150, null=True)),
                ('category', models.CharField(blank=True, default='Email', max_length=150, null=True)),
                ('due_date', models.CharField(blank=True, max_length=50, null=True)),
                ('start_date', models.CharField(blank=True, max_length=50, null=True)),
                ('reminder_date', models.CharField(blank=True, max_length=50, null=True)),
                ('progress', models.PositiveIntegerField(default=0)),
                ('priority', models.CharField(blank=True, default='Low', max_length=150, null=True)),
                ('status', models.CharField(default='Not Started', max_length=150)),
                ('related_to', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('permission', models.CharField(max_length=150)),
                ('task_owner', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
