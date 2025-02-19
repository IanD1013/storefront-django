from django.shortcuts import render
from django.db import connection
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection, Order, OrderItem
from tags.models import TaggedItem

# @transaction.atomic()
def say_hello(request):
    queryset = Product.objects.raw('SELECT * FROM store_product')

    # sometimes we want to execute queries that don't map to our model objects,
    # in those cases we can access the database directly, bypass the model layer
    with connection.cursor() as cursor: 
        cursor.execute()
        cursor.callproc('get_customers', [1, 2, 'a'])
   
    
    return render(request, 'hello.html', { 'name': 'mosh', 'result': list(queryset) })