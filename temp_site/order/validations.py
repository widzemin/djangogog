from order.models import Order
from rest_framework import serializers
from doctor.models import Doctor
from animal.models import Animal
from consts.NamesConsts import BITCH, DOG, BOTH


def validate_doctor_valid_weight(initial_data):
    doctor = Doctor.objects.get(pk=initial_data['doctor'])
    animal = Animal.objects.get(pk=initial_data['animal'])
    if animal.weight < doctor.min_animal_weight or animal.weight > doctor.max_animal_weight:
        raise serializers.ValidationError('Weight is out of range')


def validate_doctor_valid_races(initial_data):
    doctor = Doctor.objects.get(pk=initial_data['doctor'])
    animal = Animal.objects.get(pk=initial_data['animal'])
    if animal.race not in doctor.available_animal_race:
        raise serializers.ValidationError('Animal race is unavailable for this doctor')


def validate_doctor_valid_gender(initial_data):
    doctor = Doctor.objects.get(pk=initial_data['doctor'])
    animal = Animal.objects.get(pk=initial_data['animal'])
    if (animal.gender is True) and (doctor.available_animal_gender == BITCH):
        raise serializers.ValidationError('Animal gender is unavailable for this doctor')
    if (animal.gender is False) and (doctor.available_animal_gender == DOG):
        raise serializers.ValidationError('Animal gender is unavailable for this doctor')


def validate_all(initial_data):
    validate_doctor_valid_weight(initial_data)
    validate_doctor_valid_races(initial_data)
    validate_doctor_valid_gender(initial_data)
