from django.shortcuts import render
from django.http import HttpResponse
from order.models import Order
from django.template import loader

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
