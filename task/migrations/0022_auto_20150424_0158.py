# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0021_auto_20150424_0154'),
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
        migrations.AddField(
            model_name='person',
            name='my_paper',
            field=models.ForeignKey(blank=True, to='task.cs499Item', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='recommends',
            field=models.ForeignKey(blank=True, to='task.Recommendation', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 1, 58, 50, 207983, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default=b'', max_length=80),
            preserve_default=True,
        ),
    ]
