from django.shortcuts import render
from django.db.models import Value, F, Func, Count
from django.db.models import Q, F
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem, Order, Customer
from django.db.models.aggregates import Count, Sum, Avg, Max, Min

def say_hello(request):
    queryset = Customer.objects.annotate(
        orders_count=Count('order'),
    )
    
    return render(request, 'hello.html', { 'name': 'mosh', 'result': list(queryset) })