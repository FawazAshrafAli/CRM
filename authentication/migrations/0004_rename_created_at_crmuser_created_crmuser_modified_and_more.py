# Generated by Django 5.0.2 on 2024-03-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_crmuser_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crmuser',
            old_name='created_at',
            new_name='created',
        ),
        migrations.AddField(
            model_name='crmuser',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='crmuser',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='crmuser',
            name='phone',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]