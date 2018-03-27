from django.db import models

class Plodina(models.Model):
    meno = models.CharField("Názov plodiny",max_length=80, default="")