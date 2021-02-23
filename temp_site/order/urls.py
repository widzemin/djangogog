from django.urls import path, include
from order import views

urlpatterns = [
       path('<int:order_id>', views.order_list, name='order_list'),
       path('', views.index, name='index'),
] 
