from django.shortcuts import render
from .tasks import notify_customers

def say_hello(request): 
    notify_customers.delay('Heelo')
    return render(request, 'hello.html', {'name': 'Satoru'})

