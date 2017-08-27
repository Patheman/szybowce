# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('szybowce', '0008_auto_20170826_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='heading1',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='heading2',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='heading3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='heading4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='heading5',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='heading6',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='heading7',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='heading8',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='heading9',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
