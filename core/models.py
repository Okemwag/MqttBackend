import uuid
from core.types import Rule, Rules
from django.db import models
from django.contrib.auth.models import User
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class Payload(DjangoCassandraModel):
    ...


class AlertRule(models.Model):
    uid = models.UUIDField(primary_key=True, defualt=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rule = models.JSONField(default=Rule)
