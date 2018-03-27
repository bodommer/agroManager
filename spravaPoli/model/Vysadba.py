from datetime import date

from django.db import models
from django.db.models import DurationField


class Vysadba(models.Model):
    datumVysadby = models.DateField("Dátum výsadby", default = date.today())
    casVysadby = DurationField("Trvanie výsadby")
    naklady = models.PositiveIntegerField("Náklady", default=0)
    vysadeneMnozstvo = models.PositiveIntegerField("Vysadené množstvo (g)", default=0)