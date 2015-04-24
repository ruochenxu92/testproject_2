# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0027_auto_20150424_0336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='person',
            name='coauthors',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 3, 37, 1, 523226, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default=b'', max_length=80),
            preserve_default=True,
        ),
    ]
