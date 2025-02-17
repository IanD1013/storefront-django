from django.shortcuts import render
from django.db.models import Value, F, Func, Count, ExpressionWrapper, DecimalField
from django.db.models import Q, F
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem, Order, Customer
from django.db.models.aggregates import Count, Sum, Avg, Max, Min

def say_hello(request):
    discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField(max_digits=6, decimal_places=2))
    queryset = Customer.objects.annotate(discounted_price=discounted_price)
    
    return render(request, 'hello.html', { 'name': 'mosh', 'result': list(queryset) })