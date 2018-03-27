from datetime import date

from django.db import models
from django.db.models import DurationField


class Zber(models.Model):
    datumZberu = models.DateField('Dátum zberu', default = date.today())
    casZberu = DurationField("Trvanie zberu")
    uroda = models.PositiveIntegerField("Úroda", default=0)
    zisk = models.PositiveIntegerField("Zisk (eur)", default=0)
