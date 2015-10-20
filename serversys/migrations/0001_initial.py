# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20151015_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('contactperson', models.CharField(max_length=50)),
                ('contactphone', models.CharField(max_length=50)),
                ('contactemail', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='idclist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idcname', models.CharField(max_length=50)),
                ('idclevel', models.CharField(max_length=50)),
                ('idcdesc', models.CharField(max_length=255)),
                ('idcaddr', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='servers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=100)),
                ('externalip', models.CharField(max_length=150)),
                ('internalip', models.CharField(max_length=150)),
                ('virtip', models.CharField(max_length=150)),
                ('passwd', models.CharField(max_length=150)),
                ('cpu', models.CharField(max_length=50, null=True)),
                ('mem', models.CharField(max_length=50, null=True)),
                ('disk', models.CharField(max_length=50, null=True)),
                ('type', models.IntegerField(max_length=11, null=True)),
                ('system', models.IntegerField(max_length=11, null=True)),
                ('addtime', models.DateTimeField(auto_now_add=True, null=True)),
                ('comment', models.TextField(max_length=500, null=True, blank=True)),
                ('businessname', models.ForeignKey(blank=True, to='serversys.business', null=True)),
                ('dept', models.ForeignKey(blank=True, to='account.Dept', null=True)),
                ('idc', models.ForeignKey(blank=True, to='serversys.idclist', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='idclist',
            name='idczone',
            field=models.ForeignKey(blank=True, to='serversys.zone', null=True),
            preserve_default=True,
        ),
    ]
