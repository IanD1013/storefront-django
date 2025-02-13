from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem

def say_hello(request):
    queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    
    queryset = Product.objects.only('id', 'title') 
    queryset = Product.objects.defer('description') 
    
    
    return render(request, 'hello.html', {'name': 'mosh', 'products': list(queryset)})