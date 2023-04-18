import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blhserver.settings')

celery = Celery('celery')
celery.config_from_object('django.conf:settings')
celery.autodiscover_tasks()
