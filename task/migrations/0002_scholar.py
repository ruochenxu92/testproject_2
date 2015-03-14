# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('institutions', models.CharField(max_length=80, null=True, blank=True)),
                ('paper_title', models.CharField(max_length=255)),
                ('field', models.CharField(default=b'Computer Science', max_length=200)),
                ('interest', models.CharField(max_length=100)),
                ('authorUrl', models.CharField(max_length=200, null=True, blank=True)),
                ('pub_date', models.CharField(max_length=4)),
            ],
            options={
                'ordering': ('field',),
            },
            bases=(models.Model,),
        ),
    ]
