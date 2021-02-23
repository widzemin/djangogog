from django.shortcuts import render
from django.http import HttpResponse
from animal.models import Animal 
from django.template import loader

def animal_list(request, animal_id):
    try:
        animal = Animal.objects.get(pk=animal_id)
    except Animal.DoesNotExist:
        raise Http404('Animal doest not exist')
    template = loader.get_template('order/animal_item.html')
    context = {
        'animal': animal 
    }
    return HttpResponse(template.render(context, request))
