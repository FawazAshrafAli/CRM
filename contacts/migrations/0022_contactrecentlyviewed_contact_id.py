# Generated by Django 5.0.2 on 2024-03-26 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0021_remove_contactrecentlyviewed_contact_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactrecentlyviewed',
            name='contact_id',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
