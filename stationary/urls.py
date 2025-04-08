from django.urls import path
from stationary import views


urlpatterns = [
    path('stationary/', views.stationary, name='stationary'),
 
]