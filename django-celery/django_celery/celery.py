from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('django_celery')
app.conf.broker_url = 'pyamqp://guest@localhost//'
app.autodiscover_tasks()