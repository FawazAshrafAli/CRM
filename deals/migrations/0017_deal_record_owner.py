# Generated by Django 5.0.2 on 2024-04-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0016_deal_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='record_owner',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
