# Generated by Django 5.0.2 on 2024-04-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_remove_crmuser_email_remove_crmuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='crmuser',
            name='organization',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
