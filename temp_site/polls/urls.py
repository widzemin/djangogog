from django.urls import path

import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
]
