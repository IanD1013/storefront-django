from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def say_hello(request):
    queryset = Product.objects.order_by('title')
    queryset = Product.objects.order_by('-title')
    queryset = Product.objects.order_by('unit_price', '-title')
    queryset = Product.objects.order_by('unit_price', '-title').reverse()
    queryset = Product.objects.filter(collection_id=1).order_by('unit_price')

    product = Product.objects.order_by('unit_price')[0] # get the first product not query set
    product = Product.objects.earliest('unit_price') # earlist returns object, order_by returns query_set


    return render(request, 'hello.html', {'name': 'mosh', 'products': list(queryset)})