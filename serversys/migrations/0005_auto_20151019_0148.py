# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serversys', '0004_auto_20151018_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='status',
            field=models.IntegerField(default=3, max_length=11, null=True),
            preserve_default=True,
        ),
    ]
