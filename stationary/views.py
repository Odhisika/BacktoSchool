from django.shortcuts import render, redirect, get_object_or_404
from store.models import Stationary, ReviewRating

# Create your views here.

def stationary(request):
    categories = Stationary.objects.all() 
    stationary = Stationary.objects.filter(is_available=True)
    
    
    reviews_dict = {}  
    for stationary in stationary:
        reviews_dict[stationary.id] = ReviewRating.objects.filter(product_id=stationary.id, status=True)

    context = {
        'products': stationary,
        'categories': categories,
        'reviews': reviews_dict,  
        'category': 'stationary',
        'page_name': 'stationary',
    }
    return render(request, 'stationar/stationar/.html', context)