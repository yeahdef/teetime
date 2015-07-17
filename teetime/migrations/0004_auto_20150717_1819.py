# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teetime', '0003_auto_20150717_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='job',
            field=models.ForeignKey(blank=True, to='teetime.Job', null=True),
        ),
    ]
