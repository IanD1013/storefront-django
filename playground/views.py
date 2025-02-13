from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def say_hello(request):
    queryset = Product.objects.all()[:5]

    return render(request, 'hello.html', {'name': 'mosh', 'products': list(queryset)})