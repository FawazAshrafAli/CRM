# Generated by Django 5.0.2 on 2024-03-27 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0012_alter_company_date_to_remember'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='company_images/'),
        ),
    ]
