from django.urls import path
from clothing import views


urlpatterns = [
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    
    
]