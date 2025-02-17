from django.shortcuts import render
from django.db.models import Value, F
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem, Order, Customer
from django.db.models.aggregates import Count, Sum, Avg, Max, Min

def say_hello(request):
    queryset = Customer.objects.annotate(is_new=Value(True))
    queryset = Customer.objects.annotate(new_id=F('id') + 1) # reference another field
    
    return render(request, 'hello.html', { 'name': 'mosh', 'result': list(queryset) })