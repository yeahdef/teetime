# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teetime', '0011_auto_20150721_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='name',
        ),
    ]
