# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='finish',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='material',
            field=models.CharField(default=b'Your Material Link', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='sememster',
            field=models.CharField(default=b'Spring 2015', max_length=255),
            preserve_default=True,
        ),
    ]
