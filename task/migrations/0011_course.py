# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_auto_20150311_0359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('courseid', models.CharField(default=b'CS410', max_length=255)),
                ('homework', models.CharField(default=b'hw3', max_length=255)),
                ('url', models.CharField(default=b'https://wiki.cites.illinois.edu/wiki/display/timanpub/CS410S15+Schedule', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
