from django.contrib import admin

from polls.models import Doctor, Animal, Order

# Register your models here.

admin.site.register(Order)
admin.site.register(Doctor)
admin.site.register(Animal)
