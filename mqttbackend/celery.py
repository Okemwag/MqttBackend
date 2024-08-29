import os

from celery import Celery, schedules
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mqttbackend.settings")

app = Celery("mqttbackend")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    "fetch-from-influxdb": {
        "task": "core.tasks.fetch_from_influxdb",
        "schedule": schedules.crontab(minute="*/1"),
    },
    "process-alerts": {
        "task": "core.tasks.process_alerts",
        "schedule": schedules.crontab(minute="*/2"),
    }
    
}
