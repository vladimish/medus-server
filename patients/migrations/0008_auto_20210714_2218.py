# Generated by Django 3.2.5 on 2021-07-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='uuid',
        ),
        migrations.AddField(
            model_name='session',
            name='login',
            field=models.CharField(default='dad', max_length=60),
            preserve_default=False,
        ),
    ]
