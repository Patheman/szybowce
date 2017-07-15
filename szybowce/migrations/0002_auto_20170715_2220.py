# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('szybowce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='title',
            field=models.CharField(max_length=200, default=datetime.datetime(2017, 7, 15, 20, 20, 13, 123902, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weather',
            name='title',
            field=models.CharField(max_length=200, default=datetime.datetime(2017, 7, 15, 20, 20, 48, 267603, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
