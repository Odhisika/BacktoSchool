from django.shortcuts import render, redirect, get_object_or_404
from store.models import Electronics, ReviewRating

# Create your views here.

def electronics(request):
    categories = Electronics.objects.all() 
    electronics = Electronics.objects.filter(is_available=True)
    
    
    reviews_dict = {}  
    for electronic in electronics:
        reviews_dict[electronic.id] = ReviewRating.objects.filter(product_id=electronic.id, status=True)

    context = {
        'products': electronics,
        'categories': categories,
        'reviews': reviews_dict,  
        'category': 'electronics',
        'page_name': 'eclectronics',
    }
    return render(request, 'electronics/electronics/.html', context)