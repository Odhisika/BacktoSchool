
from django.shortcuts import render
from category.models import FootwearCategory
from store.models import Footwear

def mens(request):
    try:
        mens_category = FootwearCategory.objects.get(slug="mens")
        products = Footwear.objects.filter(footwear_category=mens_category, is_available=True)
    except FootwearCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'Footwear/mensF.html', context)


def ladies(request):
    try:
        
        womens_category = FootwearCategory.objects.get(slug="womens")
        products = Footwear.objects.filter(footwear_category=womens_category, is_available=True)

    except FootwearCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'Footwear/ladies.html',context) 

