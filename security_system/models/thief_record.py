from django.db import models

from security_system.models import BaseRecord


class ThiefRecord(BaseRecord):
    image = models.ImageField()
