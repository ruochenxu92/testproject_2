# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0014_auto_20150311_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sendto', models.CharField(default=b'friend1', max_length=255)),
                ('subject', models.CharField(default=b'No Subject', max_length=40)),
                ('body', models.TextField(default=b'')),
                ('attachment', models.FileField(default=None, upload_to=None, blank=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 4, 24, 1, 46, 20, 823466, tzinfo=utc))),
                ('username', models.CharField(default=b'xxu46', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
