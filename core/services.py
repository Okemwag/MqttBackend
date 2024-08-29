from core.models import Payload


class InfluxDBSerivce:

    def connect(self):
        ...

    def fetch_from_db(self, **kwargs):
        ...

    def process_data(self, data):
        ...

    def save_to_db(self, data):
        ...


class CassandraService:

    def fetch_from_db(self, **kwargs):
        payload = Payload.objects.using("cassandra").all()
        return payload
