# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_scholar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholar',
            name='author_url',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
