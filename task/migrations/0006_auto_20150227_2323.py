# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20150227_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholar',
            name='cite',
            field=models.ForeignKey(blank=True, to='task.cs499Item', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cs499item',
            name='abstract',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cs499item',
            name='authors',
            field=models.CharField(default=b'', max_length=80),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cs499item',
            name='category',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cs499item',
            name='pdflink',
            field=models.CharField(default=b'', max_length=80),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cs499item',
            name='subjects',
            field=models.CharField(default=b'', max_length=80),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cs499item',
            name='title',
            field=models.CharField(default=b'', max_length=80),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cs499item',
            name='urllink',
            field=models.CharField(default=b'', max_length=80),
            preserve_default=True,
        ),
    ]
