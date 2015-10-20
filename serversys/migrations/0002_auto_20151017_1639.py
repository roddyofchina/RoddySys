# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serversys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='contactemail',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='business',
            name='contactperson',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='business',
            name='contactphone',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='zone',
            name='name',
            field=models.CharField(default=b'\xe5\x8c\x97\xe4\xba\xac', max_length=50),
            preserve_default=True,
        ),
    ]
