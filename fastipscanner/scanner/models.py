from django.db import models
import json
from django.utils import timezone

# Create your models here.


class ScanResult(models.Model):
    ip_address = models.GenericIPAddressField()
    mac_address = models.CharField(max_length=17, unique=True)
    manufacturer = models.CharField(max_length=100, blank=True)
    alias = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    open_ports = models.TextField(blank=True)  # Store as JSON
    last_seen = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.ip_address} - {self.mac_address}"

    def set_open_ports(self, ports_dict):
        self.open_ports = json.dumps(ports_dict)

    def get_open_ports(self):
        return json.loads(self.open_ports) if self.open_ports else {}

    def update_last_seen(self):
        self.last_seen = timezone.now()
        self.save()
