# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('szybowce', '0004_auto_20170728_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='plane_speed',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='wind_speed',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
    ]
