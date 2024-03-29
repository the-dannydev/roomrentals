# Generated by Django 3.2.7 on 2021-10-15 04:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedroom', models.IntegerField(default=1)),
                ('kitchen', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=4)),
                ('bathroom', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=4)),
                ('garage', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=4)),
                ('garden', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=4)),
                ('air_condition', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=4)),
                ('extras', models.CharField(max_length=200)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]
