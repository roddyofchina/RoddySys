# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serversys', '0002_auto_20151017_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idclist',
            name='idclevel',
            field=models.IntegerField(max_length=11, null=True),
            preserve_default=True,
        ),
    ]
