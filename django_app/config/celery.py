from __future__ import absolute_import, unicode_literals
import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

app = Celery('currency_converter')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'update-rates-every-midnight': {
        'task': 'update_exchange_rates',
        'schedule': crontab(minute=0, hour=0),
    }
}
app.conf.timezone = 'Asia/Almaty'