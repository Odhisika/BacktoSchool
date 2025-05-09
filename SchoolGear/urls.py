"""
URL configuration for SchoolGear project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   
    path('securelogin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('provisions/', include('provisions.urls')),
    path('stationary/', include('stationary.urls')),
    path('electronics/', include('electronics.urls')),
    path('clothing/', include('clothing.urls')),
    path('footwear/', include('footwear.urls')),

    path('chatbot-reply/', views.chatbot_reply, name='chatbot_reply'),

    # ORDERS
    path('orders/', include('orders.urls')),


    #navigation urls
    path('books/', views.books, name='books'),
    path('provisions/', views.provisions, name='provisions'),
    path('stationary/', views.stationary, name='stationary'),
    path('electronics/', views.electronics, name='electronics'),
    path('clothing/', views.clothing, name='clothing'),
    path('footwear/', views.footwear, name='footwear'),
   


] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
