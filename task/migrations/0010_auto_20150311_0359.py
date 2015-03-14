# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_auto_20150311_0341'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='pinterest',
            new_name='PinterestItem',
        ),
    ]
