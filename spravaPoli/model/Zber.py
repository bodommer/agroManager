from django.db import models
from datetime import date, time


class Zber(models.Model):
    datumZberu = models.DateField('Dátum zberu', default = date.today())
    casZberu = models.TimeField(time(0,0,0))
    uroda = models.PositiveIntegerField("Úroda", default=0)
    zisk = models.PositiveIntegerField("Zisk (eur)", default=0)
