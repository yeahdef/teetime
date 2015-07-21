# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teetime', '0010_auto_20150721_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='percent_discount',
            field=models.IntegerField(default=0),
        ),
    ]
