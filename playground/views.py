from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def say_hello(request):
    # queryset = Product.objects.filter(inventory=F('unit_price')) 
    queryset = Product.objects.filter(inventory=F('collection__id')) 

    return render(request, 'hello.html', {'name': 'mosh', 'products': list(queryset)})