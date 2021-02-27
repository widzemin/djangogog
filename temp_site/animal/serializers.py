from animal.models import Animal
from rest_framework import serializers


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['name', 'relation_date', 'gender', 'race', 'weight']
