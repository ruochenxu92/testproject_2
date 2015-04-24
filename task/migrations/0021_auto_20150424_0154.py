# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0020_auto_20150424_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.CharField(default=b'', max_length=255)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('papers', models.ForeignKey(blank=True, to='task.cs499Item', null=True)),
            ],
            options={
                'ordering': ('customer',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 1, 54, 35, 139937, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
