from django.shortcuts import render
from store.models import Product, Customer, Collection, Order, OrderItem


def say_hello(request):  
    return render(request, 'hello.html',{'name': 'Satoru'})