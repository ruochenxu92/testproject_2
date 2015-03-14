# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_faculty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='faculty_url',
        ),
        migrations.AddField(
            model_name='faculty',
            name='email',
            field=models.EmailField(default=b'', max_length=75),
            preserve_default=True,
        ),
    ]
