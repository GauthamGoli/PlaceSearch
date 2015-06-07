# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restraunts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restraunt',
            name='coords',
        ),
        migrations.AddField(
            model_name='restraunt',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True),
            preserve_default=True,
        ),
    ]
