# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0013_course_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='username',
            field=models.CharField(default=b'xxu46', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='due_date',
            field=models.CharField(default=b'Monday', max_length=255),
            preserve_default=True,
        ),
    ]
