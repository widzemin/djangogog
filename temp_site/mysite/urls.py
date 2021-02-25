"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from order.views import (
        index, 
        order_list, 
        add_order, 
        dog_orders, 
        bitch_orders, 
        sorted_orders,
        OrderViewSet
)
from doctor.views import doctor_list
from animal.views import animal_list
import order.urls
from rest_framework import routers

router = routers.DefaultRouter()
router.register('order/setview', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include('order.urls')),
    path('doctor/<int:doctor_id>', doctor_list),
    path('animal/<int:animal_id>', animal_list),
    path('order/add/', add_order),
    path('order/dog/', dog_orders),
    path('order/bitch/', bitch_orders),
    path('order/sort/', sorted_orders),
    path('api/', include(router.urls)),
]
