# Generated by Django 5.0.2 on 2024-04-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0010_pipelinestage_remove_deal_stage_deal_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
