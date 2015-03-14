# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_auto_20150228_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='pinterest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('filename', models.CharField(default=b'', max_length=255)),
                ('course', models.CharField(default=b'ST400', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(default=b'', max_length=80),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='phone',
            field=models.CharField(default=b'', max_length=20),
            preserve_default=True,
        ),
    ]
