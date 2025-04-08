from django.urls import path
from provisions import views

urlpatterns = [
    path('bathroomHygiene/', views.bath, name='bathroomHygiene'),
    path('breakfastDrink/', views.breakfastDrink, name='breakfastDrink'),
    path('cannedMeatFish/', views.cannedMeatFish, name='cannedMeatFish'),
    path('cleaningSupplies/', views.cleanningSupplies, name='cleaningSupplies'),
    path ('cookiesBiscuits/', views.cookiesBiscuits, name='cookiesBiscuit'),
    path('dormetoryBeddingEssentials/', views.dormetryBeddingEssential, name='dormetoryBeddingEssentials'),
    path('milkSugar/', views.milkSugar, name='milkSugar'),
    path('oilTomato/', views.oilTomato, name='oilTomato'),
    path('riceNoodles/', views.riceNoodles, name='riceNoodles'),
    path('personalItemsAccessories/', views.personalItemsAccessories, name='personalItemsAcceessories'),
    path('storageUtility/', views.storageUtility, name='storageUtility'),
    path('toiletry/', views.toiletry, name='toiletry'),
    path('softdrinksjuice/', views.softdrinks, name='softdrinksjuice'),
]