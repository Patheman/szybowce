# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('szybowce', '0007_auto_20170826_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='heading1',
        ),
        migrations.RemoveField(
            model_name='route',
            name='heading2',
        ),
        migrations.RemoveField(
            model_name='route',
            name='heading3',
        ),
        migrations.RemoveField(
            model_name='route',
            name='heading4',
        ),
        migrations.RemoveField(
            model_name='route',
            name='heading5',
        ),
        migrations.RemoveField(
            model_name='route',
            name='heading6',
        ),
        migrations.RemoveField(
            model_name='route',
            name='heading7',
        ),
        migrations.RemoveField(
            model_name='route',
            name='heading8',
        ),
        migrations.RemoveField(
            model_name='route',
            name='heading9',
        ),
        migrations.AlterField(
            model_name='route',
            name='position10',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='route',
            name='position3',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='route',
            name='position4',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='route',
            name='position5',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='route',
            name='position6',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='route',
            name='position7',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='route',
            name='position8',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='route',
            name='position9',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
    ]
