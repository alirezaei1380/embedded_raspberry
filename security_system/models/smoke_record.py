from django.db import models

from security_system.models import BaseRecord


class SmokeRecord(BaseRecord):
    time = models.DateTimeField(auto_now_add=True)
