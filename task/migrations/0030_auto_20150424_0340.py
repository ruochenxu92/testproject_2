# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0029_auto_20150424_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='recommends',
            field=models.ForeignKey(blank=True, to='task.Person', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 3, 40, 25, 901968, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
