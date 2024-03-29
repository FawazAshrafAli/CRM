# Generated by Django 5.0.2 on 2024-03-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deals', '0004_delete_deal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=150)),
                ('category', models.CharField(blank=True, default='Email', max_length=150, null=True)),
                ('probability_of_winning', models.CharField(blank=True, default='Email', max_length=150, null=True)),
                ('forecast_close_date', models.DateField()),
                ('actual_close_date', models.DateField()),
                ('user_responsible', models.CharField(max_length=150)),
                ('deal_value', models.CharField(max_length=100)),
                ('bid_amount', models.CharField(max_length=50)),
                ('bid_type', models.CharField(default='Fixed Bid', max_length=100)),
                ('description', models.TextField()),
                ('tag_list', models.CharField(max_length=150)),
                ('pipeline', models.CharField(max_length=150)),
                ('stage', models.CharField(max_length=150)),
                ('visibility', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
