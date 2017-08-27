# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('szybowce', '0003_auto_20170727_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='start',
            new_name='position1',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='end',
            new_name='position10',
        ),
        migrations.AddField(
            model_name='route',
            name='position2',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='position3',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='position4',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='position5',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='position6',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='position7',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='position8',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='position9',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
