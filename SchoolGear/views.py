from django.shortcuts import render
from store.models import Product, ReviewRating, Book, Provisions, Stationary,  Footwear,  Electronics,  Clothing
from category.models import BookCategory, ProvisionCategory, FootwearCategory,  ClothingCategory
import random

def home(request):
    # Fetch a few from each category
    books = list(Book.objects.filter(is_available=True)[:3])
    provisions = list(Provisions.objects.filter(is_available=True)[:3])
    stationery = list(Stationary.objects.filter(is_available=True)[:3])
    footwear = list(Footwear.objects.filter(is_available=True)[:3])
    electronics = list(Electronics.objects.filter(is_available=True)[:3])
    clothing = list(Clothing.objects.filter(is_available=True)[:3])

    mixed_products = books + provisions + stationery + footwear + electronics + clothing
    random.shuffle(mixed_products)
    featured_products = mixed_products[:12]

    
    product_ids = [product.id for product in featured_products]
    reviews = ReviewRating.objects.filter(product_id__in=product_ids, status=True)

    context = {
        'products': featured_products,
        'reviews': reviews,
        'category': 'home',
        'page_name': 'home',
    }
    return render(request, 'home.html', context)



def books(request):
    categories = BookCategory.objects.all() 
    books = Book.objects.filter(is_available=True)
    
    
    reviews_dict = {}  
    for book in books:
        reviews_dict[book.id] = ReviewRating.objects.filter(product_id=book.id, status=True)

    context = {
        'products': books,
        'categories': categories,
        'reviews': reviews_dict,  
        'category': 'books',
        'page_name': 'books',
    }
    return render(request, 'books/books.html', context)

def provisions(request):
    categories = ProvisionCategory.objects.all() 
    provisions = Provisions.objects.filter(is_available=True)

    # Get the reviews
    reviews = None
    for product in provisions:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': provisions,
        'reviews': reviews,
        'category': 'provisions',
        'page_name': 'provisions',

    }
    return render(request, 'provision/provisions.html', context)

def stationary(request):
    stationary = Stationary.objects.filter(is_available=True)

    reviews = None  
    for product in stationary:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': stationary,
        'reviews': reviews,
        'category': 'stationary',
        'page_name': 'stationary',
    }
    return render(request, 'stationary/stationary.html', context)


def footwear(request):
    categories = FootwearCategory.objects.all() 
    footwear = Footwear.objects.filter(is_available=True)

    # Get the reviews
    reviews = None
    for product in footwear:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': footwear,
        'reviews': reviews,
        'categories': categories,
        'category': 'footwear',
        'page_name': 'footwear',
    }

    return render(request, 'footwear/footwear.html', context)


def electronics(request):
    electronics = Electronics.objects.filter(is_available=True)

    # Get the reviews
    reviews = None
    for product in electronics:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': electronics,
        'reviews': reviews,
        'category': 'electronics',
        'page_name': 'electronics',
    }

    return render(request, 'electronics/electronics.html', context)


def clothing(request):
    categories = ClothingCategory.objects.all() 
    clothing = Clothing.objects.filter(is_available=True)

    # Get the reviews
    reviews = None
    for product in clothing:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': clothing,
        'reviews': reviews,
        'categories': categories,
        'category': 'clothing',
        'page_name': 'clothing',
    }

    return render(request, 'uniform/uniform.html', context)