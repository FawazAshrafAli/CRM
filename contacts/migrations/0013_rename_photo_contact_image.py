# Generated by Django 5.0.2 on 2024-03-23 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_contact_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='photo',
            new_name='image',
        ),
    ]
