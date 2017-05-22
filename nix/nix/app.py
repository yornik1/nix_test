from __future__ import absolute_import
import os
import celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nix.settings')
app = celery.Celery('nix')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
