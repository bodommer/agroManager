from django.db import models
from spravaPoli.model.Cast import Cast
from spravaPoli.model.Plodina import Plodina
from spravaPoli.model.Zber import Zber
from spravaPoli.model.Vysadba import Vysadba

class Cyklus(models.Model):
    cast = models.ForeignKey(Cast, on_delete=models.CASCADE)
    plodina = models.ForeignKey(Plodina)
    vysadba = models.ForeignKey(Vysadba, on_delete=models.CASCADE, blank=True, null=True)
    zber = models.ForeignKey(Zber, on_delete=models.CASCADE, blank=True, null=True)