from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def say_hello(request):
    # keyword=value
    queryset1 = Product.objects.filter(unit_price=20)
    queryset2 = Product.objects.filter(unit_price__gt=20)
    queryset3 = Product.objects.filter(unit_price__range=(20, 30))
    queryset4 = Product.objects.filter(collection__id__range=(1, 2, 3))  # collection_id in (1, 2, 3)
    queryset5 = Product.objects.filter(title__icontains='coffee')        # title like '%coffee%'
    queryset6 = Product.objects.filter(title__startswith='coffee')        
    queryset7 = Product.objects.filter(last_update__year=2021)        
    queryset8 = Product.objects.filter(description__isnull=True)        

    return render(request, 'hello.html', {'name': 'mosh', 'products': list(queryset5)})