# Generated by Django 5.0.2 on 2024-04-15 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0023_alter_crmusereducation_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crmuserexperience',
            old_name='completed_month',
            new_name='completed_month_and_year',
        ),
        migrations.RenameField(
            model_name='crmuserexperience',
            old_name='started_year',
            new_name='started_month_and_year',
        ),
        migrations.RemoveField(
            model_name='crmuserexperience',
            name='completed_year',
        ),
        migrations.RemoveField(
            model_name='crmuserexperience',
            name='stated_month',
        ),
    ]
