# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serversys', '0003_auto_20151018_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='servers',
            name='cpumhz',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servers',
            name='status',
            field=models.IntegerField(max_length=11, null=True),
            preserve_default=True,
        ),
    ]
