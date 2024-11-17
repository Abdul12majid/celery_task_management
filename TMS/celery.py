from __future__ import absolute_import, unicode_literals
import os, ssl
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TMS.settings')

app = Celery('TMS',
     broker_use_ssl = {
        'ssl_cert_reqs': ssl.CERT_NONE
     },
     redis_backend_use_ssl = {
        'ssl_cert_reqs': ssl.CERT_NONE
     }
)

# Configure Celery with the namespace 'CELERY'
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks from all registered Django apps.
app.autodiscover_tasks()
