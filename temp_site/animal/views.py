from django.shortcuts import render
from django.http import HttpResponse, Http404
from animal.models import Animal 
from django.template import loader
from rest_framework import viewsets
from rest_framework import permissions
from animal.serializers import AnimalSerializer


def animal_list(request, animal_id):
    try:
        animal = Animal.objects.get(pk=animal_id)
    except Animal.DoesNotExist:
        raise Http404('Animal doest not exist')
    template = loader.get_template('animal/animal_item.html')
    context = {
        'animal': animal 
    }
    return HttpResponse(template.render(context, request))


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated]
