# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0012_auto_20150311_0555'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='due_date',
            field=models.CharField(default=b'1 Monday', max_length=255),
            preserve_default=True,
        ),
    ]
