# Generated by Django 5.0.2 on 2024-04-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0014_remove_crmuser_education_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='crmuser',
            name='education_info',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
