from django.urls import path

import views

urlpatterns = [
    path('<int:animal_id>/', views.animal_list, name='animal'),
]
