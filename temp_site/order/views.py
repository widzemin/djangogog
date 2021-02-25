from django.shortcuts import render
from django.http import HttpResponse, Http404
from order.models import Order
from django.template import loader
from django.forms import modelform_factory
from order.forms import OrderForm
from rest_framework import viewsets
from rest_framework import permissions
from order.serializers import OrderSerializer


def index(request):
    try:
        orders = Order.objects.all()
    except Order.DoesNotExist:
        raise Http404('Order does not exist')    
    template = loader.get_template('order/index.html')
    context = {
        'orders': orders,
    }        
    return HttpResponse(template.render(context, request)) 


def order_list(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        raise Http404('Order does not exist')
    template = loader.get_template('order/order_item.html')
    context = {
        'order': order,
    }
    return HttpResponse(template.render(context, request))


def add_order(request):
    order_formset = modelform_factory(Order, form=OrderForm)
    if request.method == 'POST':
        formset = order_formset(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        formset = order_formset()
    return render(request, 'order/order_form.html', {'formset': formset})


def dog_orders(request):
    try:
        orders = Order.objects.filter(animal__gender=True)
    except Order.DoesNotExist:
        raise Http404('Order does not exist')
    template = loader.get_template('order/index.html')
    context = {
        'orders': orders,
    }
    return HttpResponse(template.render(context, request))


def bitch_orders(request):
    try:
        orders = Order.objects.filter(animal__gender=False)
    except Order.DoesNotExist:
        raise Http404('Order does not exist')
    template = loader.get_template('order/index.html')
    context = {
        'orders': orders,
    }
    return HttpResponse(template.render(context, request))


def sorted_orders(request):
    try:
        orders = Order.objects.order_by('-date')
    except Order.DoesNotExist:
        raise Http404('Order does not exist')
    template = loader.get_template('order/index.html')
    context = {
        'orders': orders,
    }
    return HttpResponse(template.render(context, request))


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]




