# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0024_auto_20150424_0334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='papers',
        ),
        migrations.AlterModelOptions(
            name='person',
            options={},
        ),
        migrations.RemoveField(
            model_name='person',
            name='coauthors',
        ),
        migrations.RemoveField(
            model_name='person',
            name='my_paper',
        ),
        migrations.RemoveField(
            model_name='person',
            name='recommends',
        ),
        migrations.DeleteModel(
            name='Recommendation',
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 3, 34, 26, 581462, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
    ]
