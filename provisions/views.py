from django.shortcuts import render
from category.models import ProvisionCategory
from store.models import Provisions, ReviewRating

# Create your views here.
def bath(request):
    try:
        
        bath_category = ProvisionCategory.objects.get(slug="bathroom-and-hygiene-supplies")
        products = Provisions.objects.filter(provision_category=bath_category, is_available=True)

    except ProvisionCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'provision/bathroomHygiene.html',context) 

def breakfastDrink(request):
    try:
        
        breakfast_category = ProvisionCategory.objects.get(slug="breakfast-drinks")
        products = Provisions.objects.filter(provision_category=breakfast_category, is_available=True)

    except ProvisionCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'provision/breakFastDringks.html',context)

def cannedMeatFish(request):
    try:
        
        canned_category = ProvisionCategory.objects.get(slug="canned-meat-and-fish")
        products = Provisions.objects.filter(provision_category=canned_category, is_available=True)

    except ProvisionCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'provision/cannnedMeatFish.html',context)

def cleanningSupplies(request):
    try:
        
        cleaning_category = ProvisionCategory.objects.get(slug="cleaning-supplies")
        products = Provisions.objects.filter(provision_category=cleaning_category, is_available=True)

    except ProvisionCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'provision/cleaningSupplies.html',context)

def cookiesBiscuits(request):
    try:
        cookies_category = ProvisionCategory.objects.get(slug="cookies-and-biscuits")
        products = Provisions.objects.filter(provision_category=cookies_category, is_available=True)
    except ProvisionCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'provision/cookiesBiscouit.html', context)


def dormetryBeddingEssential(request):
    try:
        
        dormitory_category = ProvisionCategory.objects.get(slug="dormitory-and-bedding-essentials")
        products = Provisions.objects.filter(provision_category=dormitory_category, is_available=True)

    except ProvisionCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'provision/dormetryBeddingEssential.html',context)

def milkSugar(request):
    try:
        
        milk_category = ProvisionCategory.objects.get(slug="milk-and-sugar")
        products = Provisions.objects.filter(provision_category=milk_category, is_available=True)

    except ProvisionCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'provision/milkSugar.html',context)

def oilTomato(request):
    try:
        
        oil_category = ProvisionCategory.objects.get(slug="oil-and-tomato-paste")
        products = Provisions.objects.filter(provision_category=oil_category, is_available=True)

    except ProvisionCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'provision/oilTomato.html',context)

def personalItemsAccessories(request):
    try:
        
        personal_category = ProvisionCategory.objects.get(slug="personal-items-and-accessories")
        products = Provisions.objects.filter(provision_category=personal_category, is_available=True)

    except ProvisionCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'provision/personalItemsAcceessories.html',context)

def riceNoodles(request):
    try:
        
        rice_category = ProvisionCategory.objects.get(slug="rice-and-noodles")
        products = Provisions.objects.filter(provision_category=rice_category, is_available=True)

    except ProvisionCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'provision/riceNoodles.html',context)

def storageUtility(request):
    try:
        
        storage_category = ProvisionCategory.objects.get(slug="storage-supplies")
        products = Provisions.objects.filter(provision_category=storage_category, is_available=True)

    except ProvisionCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'provision/storageUtility.html',context)

def toiletry(request):
    try:
        
        toiletry_category = ProvisionCategory.objects.get(slug="toiletrys-and-sanitary-pads")
        products = Provisions.objects.filter(provision_category=toiletry_category, is_available=True)

    except ProvisionCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'provision/toiletry.html',context)

def softdrinks(request):
    try:
        
        softdrink_category = ProvisionCategory.objects.get(slug="soft-drinks-and-juice")
        products = Provisions.objects.filter(provision_category=softdrink_category, is_available=True)

    except ProvisionCategory.DoesNotExist:
        products = []  

    context = {
        'products': products
    }
    return render(request, 'provision/softdrinksjuice.html',context)