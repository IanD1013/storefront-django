from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem

def say_hello(request):
    collection = Collection.objects.get(pk=11) # get the collection from database first
    collection.featured_product = None
    collection.save()

    # another way to do the same thing
    Collection.objects.filter(pk=11).update(featured_product=None) 
  
    
    return render(request, 'hello.html', { 'name': 'mosh' })