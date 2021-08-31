from __future__ import absolute_import, unicode_literals
import os

#django beat celery 

from celery import Celery
from django.conf import settings
#from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockproject.settings')

app = Celery('stockproject')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'every-10-seconds':{   #to req every 10 secs
        'task': 'mainapp.tasks.update_stock',   #call that function
        'schedule' : 10,  #every 10 secs schedule it
    }
}

