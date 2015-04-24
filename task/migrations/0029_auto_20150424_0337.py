# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0028_auto_20150424_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='cs499item',
            name='my_paper',
            field=models.ForeignKey(blank=True, to='task.Person', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 3, 37, 39, 265606, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
