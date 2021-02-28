from django.db import models
from consts.NamesConsts import MOPS, RACES
import datetime


class Animal(models.Model):
    name = models.CharField(max_length=100)
    relation_date = models.DateField(auto_now=False, default=datetime.date.today())
    gender = models.BooleanField(default=True)
    race = models.CharField(max_length=100, choices=RACES, default=MOPS)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.name
