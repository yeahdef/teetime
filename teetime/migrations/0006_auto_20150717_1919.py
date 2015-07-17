# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teetime', '0005_auto_20150717_1912'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='State',
            new_name='JobState',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='status',
            new_name='state',
        ),
    ]
