from django.shortcuts import render
from django.http import HttpResponse
from order.models import Order
from django.template import loader

def index(request):
    try:
        orders = Order.objects.all()
    except Question.DoesNotExist:
        raise Http404('Question does not exist')    
    output = ''
    for order in orders:
        output = (output + ' ' + 
                order.Animal.name + ' ' + 
                order.Doctor.name + ' ' +  
                str(order.date) + ' ' +  
                order.reason + '<br>')
    template = loader.get_template('order/index.html')
    context = {
        'orders': orders,
    }        
    return HttpResponse(template.render(context, request)) 

