# Generated by Django 3.2.5 on 2021-07-11 17:57

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_patient_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_receipt',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 11, 20, 57, 22, 437700)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='uuid',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
