# Generated by Django 3.1.3 on 2020-11-26 13:35

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='DEPARTEMENT_a_CONTACTER',
            field=models.TextField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='send_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 11, 26, 13, 34, 59, 242001, tzinfo=utc)),
        ),
    ]
