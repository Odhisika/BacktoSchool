from django.contrib import admin
from .models import Book, Product, Electronics, Clothing, Provisions,  Footwear, Stationary, Variation, ReviewRating, ProductGallery
import admin_thumbnails
from django.core.exceptions import ValidationError

def clean(self):
    if not isinstance(self.product, (Clothing, Footwear)):
        raise ValidationError("Variations can only be used for Clothing or Footwear products.")


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

# Admin for all product-based sub-models
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

# Register each sub-model individually
admin.site.register(Product, ProductAdmin)
admin.site.register(Book, ProductAdmin)
admin.site.register(Electronics, ProductAdmin)
admin.site.register(Clothing, ProductAdmin)
admin.site.register( Footwear, ProductAdmin)
admin.site.register(Stationary, ProductAdmin)
admin.site.register(Provisions, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
