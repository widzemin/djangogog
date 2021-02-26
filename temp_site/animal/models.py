from django.db import models
from consts.NamesConsts import RACES


class Animal(models.Model):
    name = models.CharField(max_length=100)
    relation_date = models.DateField()
    gender = models.BooleanField()
    race = models.CharField(max_length=100, choices=RACES)

    def __str__(self):
         return self.name
