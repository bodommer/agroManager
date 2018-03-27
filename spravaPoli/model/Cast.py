from django.db import models
from spravaPoli.model.Pozemok import Pozemok

class Cast(models.Model):
    meno = models.CharField(max_length=80, default="")
    rozloha = models.PositiveIntegerField(default=0)
    pouzivany = models.BooleanField(default=True)
    pozemok = models.ForeignKey(Pozemok, on_delete=models.CASCADE)