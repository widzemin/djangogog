from django.shortcuts import render
from django.http import HttpResponse, Http404
from doctor.models import Doctor
from django.template import loader
from rest_framework import viewsets
from rest_framework import permissions
from doctor.serializers import DoctorSerializer


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


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
