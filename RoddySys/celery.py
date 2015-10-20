from __future__ import absolute_import
#coding:utf8

import os
import django
django.setup()

from celery import Celery,platforms
from datetime import timedelta

platforms.C_FORCE_ROOT = True

from serversys.models import *


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RoddySys.settings')

from django.conf import settings

app = Celery('RoddySys')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



#定义监控数据每60秒执行一次
app.conf.update(
    CELERYBEAT_SCHEDULE = {
        "runping": {
                "task": "serversys.tasks.runping",
                "schedule": timedelta(seconds=60),
                },
        }
)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))