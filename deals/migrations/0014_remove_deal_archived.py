# Generated by Django 5.0.2 on 2024-04-01 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0013_alter_deal_user_responsible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='archived',
        ),
    ]