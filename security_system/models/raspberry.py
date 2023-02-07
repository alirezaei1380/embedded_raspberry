from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Raspberry(models.Model):

    admin_code = models.IntegerField()

    user_code = models.IntegerField()
