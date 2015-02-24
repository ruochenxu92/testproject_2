# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, blank=True)),
                ('body', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published', blank=True)),
                ('likes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='cs499Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('urllink', models.CharField(max_length=80, null=True, blank=True)),
                ('pdflink', models.CharField(max_length=80, null=True, blank=True)),
                ('title', models.CharField(max_length=80, null=True, blank=True)),
                ('authors', models.CharField(max_length=80, null=True, blank=True)),
                ('subjects', models.CharField(max_length=80, null=True, blank=True)),
                ('abstract', models.TextField()),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('category', models.CharField(max_length=200, null=True, blank=True)),
                ('likes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('date',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80, null=True, blank=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('pubDate', models.DateTimeField(null=True, blank=True)),
                ('citedTimes', models.IntegerField(default=0)),
                ('paperUrl', models.CharField(max_length=200, null=True, blank=True)),
                ('author', models.CharField(max_length=80, null=True, blank=True)),
                ('institution', models.CharField(max_length=80, null=True, blank=True)),
                ('field', models.CharField(max_length=80, null=True, blank=True)),
                ('interest', models.CharField(max_length=80, null=True, blank=True)),
                ('authorUrl', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'ordering': ('author',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='description',
            name='taskName',
            field=models.ForeignKey(to='task.Task', blank=True),
            preserve_default=True,
        ),
    ]
