
from django.contrib import admin
from .models import Category, BookCategory, FootwearCategory, ClothingCategory, ProvisionCategory


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')


class BookCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('book_category',)}
    list_display = ('book_category', 'slug')


class FootwearCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('footwear_category',)}
    list_display = ('footwear_category', 'slug')

class ClothingCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('clothing_category',)}
    list_display = ('clothing_category', 'slug')

class ProvisionCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('provision_category',)}
    list_display = ('provision_category', 'slug')


admin.site.register(Category, CategoryAdmin)
admin.site.register(BookCategory, BookCategoryAdmin)
admin.site.register(FootwearCategory, FootwearCategoryAdmin)
admin.site.register(ClothingCategory, ClothingCategoryAdmin)
admin.site.register(ProvisionCategory, ProvisionCategoryAdmin)
admin.site.site_header = "BackToSchool Admin"

# Register 