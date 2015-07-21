# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teetime', '0009_auto_20150721_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
