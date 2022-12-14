# Generated by Django 3.2.4 on 2022-08-13 09:58

import application.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_date', models.DateField(default=datetime.datetime.now, validators=[application.models.validate_date])),
            ],
        ),
        migrations.CreateModel(
            name='Executive',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('joining_date', models.DateField()),
                ('equipment_name', models.ManyToManyField(to='application.Equipment')),
            ],
        ),
    ]
