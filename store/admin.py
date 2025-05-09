from django.contrib import admin
from .models import Book, Product, Electronics, FootSize, Size, Color, Clothing, Provisions,  Footwear, Stationary, ReviewRating, ProductGallery
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(FootSize)
class FootSizeAdmin(admin.ModelAdmin):
    list_display = ['number']

# Admin for all product-based sub-models
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

class FootwearAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'shoe_type']
    filter_horizontal = ('colors', 'sizes')

class ClothingAdmin(admin.ModelAdmin):
    list_display = ['product_name']
    filter_horizontal = ('colors', 'sizes')



# Register each sub-model individually
admin.site.register(Product, ProductAdmin)
admin.site.register(Book, ProductAdmin)
admin.site.register(Electronics, ProductAdmin)
admin.site.register(Clothing, ProductAdmin)
admin.site.register( Footwear, ProductAdmin)
admin.site.register(Stationary, ProductAdmin)
admin.site.register(Provisions, ProductAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
