# Generated by Django 5.0.2 on 2024-02-27 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='pipeline',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
