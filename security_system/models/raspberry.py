from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Raspberry(models.Model):

    admin_code = models.IntegerField(
        validators=[
            MinValueValidator(100_000),
            MaxValueValidator(900_000_000),
        ],
    )

    user_code = models.IntegerField(
        validators=[
            MinValueValidator(100_000),
            MaxValueValidator(900_000_000),
        ],
    )
