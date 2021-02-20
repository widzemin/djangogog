from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Order
from django.template import loader

# Create your views here.

def index(request):
    orders = Order.objects.all()
    output = ''
    for q in orders:
        output = (output + ' ' + 
                q.Animal.Name + ' ' + 
                q.Doctor.Name + ' ' +  
                str(q.Date) + ' ' +  
                q.Reason + '<br>')
    template = loader.get_template('polls/intex.html')
    context = {
            'orders': orders,
            }        
    return HttpResponse(template.render(context, request)) 

