from django.db import models
from consts.NamesConsts import GRADES

class Doctor(models.Model):
    name = models.TextField()
    grade = models.CharField(max_length=100, choices = GRADES)

    def __str__(self):
        return self.name
