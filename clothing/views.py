from django.shortcuts import render, get_object_or_404
from category.models import BookCategory, Category, ClothingCategory
from store.models import Product, Book, ReviewRating, Clothing
# Create your views here.


def men(request):
    try:
        
        men_category = ClothingCategory.objects.get(slug="men")
        products = Clothing.objects.filter(clothing_category=men_category, is_available=True)

    except ClothingCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'uniform/men.html',context) 



def women(request):
    try:
        
        men_category = ClothingCategory.objects.get(slug="women")
        products = Clothing.objects.filter(clothing_category=men_category, is_available=True)

    except ClothingCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'uniform/women.html',context) 

