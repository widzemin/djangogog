from order.models import Order
from rest_framework import serializers
from doctor.models import Doctor
from animal.models import Animal


def validate_weight(initial_data):
    doctor = Doctor.objects.get(pk=initial_data['doctor'])
    animal = Animal.objects.get(pk=initial_data['animal'])
    if animal.weight < doctor.min_animal_weight or animal.weight > doctor.max_animal_weight:
        raise serializers.ValidationError('Weight is out of range')


def validate_all(initial_data):
    validate_weight(initial_data)
