from django.db import models

class Coin(models.Model):
    value = models.IntegerField()


class Solution(models.Model):
    coin = models.ForeignKey(Coin)
    solution = models.IntegerField()
