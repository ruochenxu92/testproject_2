# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20150227_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('field', models.CharField(default=b'Computer Science', max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('faculty_url', models.CharField(default=b'', max_length=200)),
                ('institution', models.CharField(default=b'University of Illinios at Urbana-Champaign', max_length=100)),
            ],
            options={
                'ordering': ('field',),
            },
            bases=(models.Model,),
        ),
    ]
