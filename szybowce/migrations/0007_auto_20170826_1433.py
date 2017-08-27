# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('szybowce', '0006_route_wind_angle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='heading',
            new_name='heading1',
        ),
        migrations.AddField(
            model_name='route',
            name='heading2',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='route',
            name='heading3',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='route',
            name='heading4',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='route',
            name='heading5',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='route',
            name='heading6',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='route',
            name='heading7',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='route',
            name='heading8',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='route',
            name='heading9',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='route',
            name='position10',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='route',
            name='position3',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='route',
            name='position4',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='route',
            name='position5',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='route',
            name='position6',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='route',
            name='position7',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='route',
            name='position8',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='route',
            name='position9',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
    ]
