from django.db import models

class Coin(models.Model):
    value = models.IntegerField()
