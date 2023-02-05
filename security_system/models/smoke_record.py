from django.db import models

from security_system.models import BaseRecord


class SmokeRecord(BaseRecord):
    methan = models.FloatField()
    hydrogen = models.FloatField()
    lpg = models.FloatField()
    smoke = models.FloatField()
