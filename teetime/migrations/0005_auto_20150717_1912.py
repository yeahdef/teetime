# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teetime', '0004_auto_20150717_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='product',
            field=models.ForeignKey(blank=True, to='teetime.Product', null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='delivered_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
