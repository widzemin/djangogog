from django.db import models
from consts.NamesConsts import (
    MOPS, RACES,
    DOCTOR, GRADES,
    BOTH, GENDERS
)
from rest_framework import serializers
from multiselectfield import MultiSelectField


class Doctor(models.Model):
    name = models.TextField()
    grade = models.CharField(max_length=100, choices=GRADES, default=DOCTOR)
    min_animal_weight = models.IntegerField(default=0)
    max_animal_weight = models.IntegerField(default=0)
    available_animal_race = MultiSelectField(choices=RACES, default=MOPS)
    available_animal_gender = models.CharField(max_length=100, choices=GENDERS, default=BOTH)

    def __str__(self):
        return self.name
