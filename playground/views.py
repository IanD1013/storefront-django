from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem

def say_hello(request):
    # first need to fint the content type id for the product model
    content_type = ContentType.objects.get_for_model(Product)

    # next we can use the content type id to filter the tagged items
    queryset = TaggedItem.objects \
        .select_related('tag') \
        .filter(
            content_type=content_type, 
            object_id=1
        )
    
    return render(request, 'hello.html', { 'name': 'mosh', 'tags': list(queryset) })