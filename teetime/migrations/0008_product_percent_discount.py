# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teetime', '0007_auto_20150717_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='percent_discount',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
