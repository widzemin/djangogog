from order.models import Order
from rest_framework import serializers
from doctor.models import Doctor
from animal.models import Animal
from order.validations import validate_all


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['reason', 'date', 'doctor', 'animal']

    def validate(self, data):
        validate_all(self.initial_data)
        return data

    #def validate_doctor(self, doctor):
    #    animal = Animal.objects.get(pk=self.initial_data['animal'])
    #    if animal.weight < doctor.min_animal_weight or animal.weight > doctor.max_animal_weight:
    #        raise serializers.ValidationError('Weight is out of range')
    #    return doctor
