from django.urls import path
from . import views

urlpatterns = [
    path('books/<slug:category_slug>/', views.books_by_category, name='products_by_book_category'),
]
