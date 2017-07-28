# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('szybowce', '0002_auto_20170715_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='end_lat',
        ),
        migrations.RemoveField(
            model_name='route',
            name='end_long',
        ),
        migrations.RemoveField(
            model_name='route',
            name='start_lat',
        ),
        migrations.RemoveField(
            model_name='route',
            name='start_long',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='temparature',
        ),
        migrations.AddField(
            model_name='route',
            name='end',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='heading',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='start',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weather',
            name='temperature',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='weather',
            name='pressure',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weather',
            name='wind',
            field=models.FloatField(),
        ),
    ]
