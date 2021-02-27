from doctor.models import Doctor
from rest_framework import serializers


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['name', 'grade', 'min_animal_weight', 'max_animal_weight']
