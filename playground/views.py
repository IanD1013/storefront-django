from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem

def say_hello(request):
    queryset = Product.objects.all()
    list(queryset)
    queryset[0]
    
    return render(request, 'hello.html', { 'name': 'mosh', 'tags': list(queryset) })