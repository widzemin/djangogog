from django.urls import path

import views

urlpatterns = [
    path('<int:doctor_id>/', views.doctor_id, name='doctor'),
]
