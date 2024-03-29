# Generated by Django 5.0.2 on 2024-03-06 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0005_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('organization', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('email_opted_out', models.BooleanField(default=False)),
                ('phone', models.CharField(max_length=16)),
                ('home_phone', models.CharField(blank=True, max_length=16, null=True)),
                ('mobile_phone', models.CharField(max_length=16)),
                ('other_phone', models.CharField(blank=True, max_length=16, null=True)),
                ('assistant_phone', models.CharField(blank=True, max_length=16, null=True)),
                ('assistant_name', models.CharField(blank=True, max_length=150, null=True)),
                ('fax', models.CharField(blank=True, max_length=25, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('mailing_address', models.TextField()),
                ('mailing_city', models.CharField(blank=True, max_length=50, null=True)),
                ('mailing_state', models.CharField(blank=True, max_length=50, null=True)),
                ('mailing_postal_code', models.CharField(blank=True, max_length=15, null=True)),
                ('mailing_country', models.CharField(blank=True, default='India', max_length=100, null=True)),
                ('other_address', models.TextField()),
                ('other_city', models.CharField(blank=True, max_length=50, null=True)),
                ('other_state', models.CharField(blank=True, max_length=50, null=True)),
                ('other_postal_code', models.CharField(blank=True, max_length=15, null=True)),
                ('other_country', models.CharField(blank=True, default='India', max_length=100, null=True)),
                ('due_date', models.DateField()),
                ('date_of_birth', models.DateField()),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('permission', models.CharField(blank=True, max_length=100, null=True)),
                ('tag_list', models.CharField(max_length=150)),
                ('task_visibility', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
