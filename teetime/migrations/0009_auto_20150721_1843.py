# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teetime', '0008_product_percent_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1, max_length=10)),
                ('job', models.ForeignKey(to='teetime.Job')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='job',
        ),
        migrations.AddField(
            model_name='product',
            name='lot',
            field=models.ForeignKey(blank=True, to='teetime.Lot', null=True),
        ),
    ]
