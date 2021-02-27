from django.db import models
from consts.NamesConsts import RACES


class Animal(models.Model):
    name = models.CharField(max_length=100)
    relation_date = models.DateField(auto_now=False)
    gender = models.BooleanField()
    race = models.CharField(max_length=100, choices=RACES)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.name
