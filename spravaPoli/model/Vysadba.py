from django.db import models
from datetime import date, time


class Vysadba(models.Model):
    datumVysadby = models.DateField("Datum vysadby", default = date.today())
    casVysadby = models.TimeField(time(0,0,0))
    naklady = models.PositiveIntegerField("Naklady", default=0)
    vysadeneMnozstvo = models.PositiveIntegerField("Vysadene mnozstvo (g)", default=0)