from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem, Order
from django.db.models.aggregates import Count, Sum, Avg, Max, Min

def say_hello(request):
    result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))
    result = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))
    
    return render(request, 'hello.html', { 'name': 'mosh', 'result': result })