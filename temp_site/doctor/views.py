from django.shortcuts import render
from django.http import HttpResponse
from doctor.models import Doctor
from django.template import loader

def doctor_list(request, doctor_id):
    try:
        doctor = Doctor.objects.get(pk=doctor_id)
    except Doctor.DoesNotExist:
        raise Http404('Doctor doest not exist')
    template = loader.get_template('doctor/doctor_item.html')
    context = {
        'doctor': doctor
    }
    return HttpResponse(template.render(context, request)) 
