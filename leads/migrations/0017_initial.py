# Generated by Django 5.0.2 on 2024-03-14 10:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0003_crmuser_created_at'),
        ('leads', '0016_delete_lead'),
        ('organizations', '0010_remove_company_billing_street'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=25)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=150)),
                ('lead_status', models.CharField(default='OPEN - Not Contacted', max_length=150)),
                ('lead_rating', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('email_opted_out', models.BooleanField(default=False)),
                ('phone', models.CharField(max_length=20)),
                ('mobile_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('fax', models.CharField(blank=True, max_length=20, null=True)),
                ('website', models.CharField(blank=True, max_length=150, null=True)),
                ('industry', models.CharField(blank=True, max_length=150, null=True)),
                ('number_of_employees', models.CharField(blank=True, max_length=50, null=True)),
                ('lead_source', models.CharField(blank=True, default='Web', max_length=150, null=True)),
                ('mailing_address', models.TextField()),
                ('mailing_city', models.CharField(max_length=50)),
                ('mailing_state', models.CharField(max_length=50)),
                ('mailing_postal_code', models.CharField(max_length=15)),
                ('mailing_country', models.CharField(default='India', max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('tag_list', models.CharField(blank=True, max_length=150, null=True)),
                ('permission', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('lead_owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lead_owner', to='authentication.crmuser')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organizations.company')),
                ('user_responsible', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_responsible', to='authentication.crmuser')),
            ],
        ),
    ]