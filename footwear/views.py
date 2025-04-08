
from django.shortcuts import render
from category.models import FootwearCategory
from store.models import Footwear
# Create your views here.


def mens(request):
    try:
        
        men_category = FootwearCategory.objects.get(slug="men")
        products = FootwearCategory.objects.filter(men_type=men_category, is_available=True)

    except FootwearCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'Footwear/mensF.html',context) 



def ladies(request):
    try:
        
        men_category = FootwearCategory.objects.get(slug="women")
        products = Footwear.objects.filter(men_type=men_category, is_available=True)

    except FootwearCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'Footwear/ladies.html',context) 

