# Generated by Django 5.0.2 on 2024-03-20 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_pipelinestage_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pipelinestage',
            options={'ordering': ['created']},
        ),
    ]
