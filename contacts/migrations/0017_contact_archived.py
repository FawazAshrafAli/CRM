# Generated by Django 5.0.2 on 2024-03-25 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0016_alter_contact_date_of_birth_alter_contact_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]