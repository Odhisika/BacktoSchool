from django.shortcuts import render, get_object_or_404
from category.models import  BookCategory  
from store.models import ReviewRating , Book 

def books_by_category(request, category_slug):
    category = get_object_or_404(BookCategory, slug=category_slug)
    books = Book.objects.filter(book_category=category, is_available=True)

    reviews_dict = {
        book.id: ReviewRating.objects.filter(product_id=book.id, status=True)
        for book in books
    }

    context = {
        'products': books,
        'category': category,
        'reviews': reviews_dict,
        'page_name': f'{category.book_category} Books',
    }

    template_map = {
        'kg': 'books/kg.html',
        'primary': 'books/primary.html',
        'jhs': 'books/jhs.html',
        'shs': 'books/shs.html',
    }

    # Always return a template — even if the slug is invalid
    template_name = template_map.get(category_slug)

    if template_name:
        return render(request, template_name, context)
    else:
        # Fallback for invalid slug
        return render(request, 'books/no_books.html', {
            'page_name': 'Category Not Found',
            'message': 'This category does not exist or currently has no books available.'
        })
