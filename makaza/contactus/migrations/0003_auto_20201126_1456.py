# Generated by Django 3.1.3 on 2020-11-26 13:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0002_auto_20201126_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='DEPARTEMENT_a_CONTACTER',
        ),
        migrations.AlterField(
            model_name='contactus',
            name='send_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 11, 26, 13, 56, 26, 794737, tzinfo=utc)),
        ),
    ]
