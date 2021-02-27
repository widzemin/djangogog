from django.db import models
from consts.NamesConsts import GRADES


class Doctor(models.Model):
    name = models.TextField()
    grade = models.CharField(max_length=100, choices=GRADES)
    min_animal_weight = models.IntegerField(default=0)
    max_animal_weight = models.IntegerField(default=0)

    def __str__(self):
        return self.name
