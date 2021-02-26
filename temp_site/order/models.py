from django.db import models
from animal.models import Animal
from doctor.models import Doctor
import datetime


class Order(models.Model):
    reason = models.TextField()
    date = models.DateTimeField(auto_now=False)
    doctor = models.ForeignKey(
            Doctor,
            on_delete=models.CASCADE,
    )
    animal = models.ForeignKey(
            Animal,
            on_delete=models.CASCADE,
    )
    
    def is_active(self):
        return self.date >= datetime.datetime.now()
