from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem, Order

def say_hello(request):
    # selected_related (1)
    # prefetch_related (n)
    # queryset = Product.objects.select_related('collection').all()  
    # queryset = Product.objects.select_related('collection__someOtherField').all()  
    # queryset = Product.objects.prefetch_related('promotions').all()  
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()  
    
    # Get the last 5 orders with their customer and items (incl product)
    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    
    return render(request, 'hello.html', { 'name': 'mosh' })