from django.db import models
from .consts import RACES, GRADES, MOPS, DOCTOR 
 

# Create your models here

class Animal(models.Model):
    Name = models.CharField(max_length=100)
    CreationDate = models.DateField()
    Gender = models.BooleanField()
    Race = models.CharField(max_length=100, choices=RACES)

class Doctor(models.Model):
    Name = models.TextField()
    Grade = models.CharField(max_length=100, choices = GRADES)
    
class Order(models.Model):
    Reason = models.TextField()
    Date = models.DateTimeField(auto_now=True)
    Doctor = models.ForeignKey(
            'Doctor', 
            on_delete=models.CASCADE,                    
    )
    Animal = models.ForeignKey(
            'Animal',
            on_delete=models.CASCADE,
    )

    
