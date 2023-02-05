from django.db import models


class BaseRecord(models.Model):
    time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
