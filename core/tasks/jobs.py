from core.models import AlertRule, Payload
from core.services import CassandraService, InfluxDBSerivce
from celery import shared_task


@shared_task
def fetch_from_influxdb():
    service = InfluxDBSerivce()
    data: list[dict] = service.fetch_from_db()
    for obj in data:
        identifer = obj.get("id")
        value = obj.get("value")
        previous = obj.get("previous")
        Payload.objects.using("cassandra").create(
        )
    return "Data fetched from InfluxDB"


@shared_task
def process_alerts():
    data = CassandraService()
    for obj in data:
        alert = AlertRule.objects.filter(name__iexact=obj.get("id")).first()
        rule = alert.rule
        if rule["normal_value"] < value:
            # send email
            pass
