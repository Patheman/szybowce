# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('szybowce', '0005_auto_20170802_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='wind_angle',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
