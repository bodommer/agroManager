from django.db import models

class Pozemok(models.Model):
    meno = models.CharField(max_length=80, default="")
    rozloha = models.PositiveIntegerField(default=0)