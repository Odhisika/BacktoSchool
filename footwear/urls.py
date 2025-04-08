from django.urls import path
from footwear import views


urlpatterns = [
    path('men/', views.mens, name='mens'),
    path('women/', views.ladies, name='ladies'),
    
    
]