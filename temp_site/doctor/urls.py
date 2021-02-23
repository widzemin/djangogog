from django.urls import path

import views

urlpatterns = [
    path('doctor_id/', views.doctor_id, name='doctor'),
]
