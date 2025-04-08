

from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
            return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name

class BookCategory(models.Model):
    book_category = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'book category'
        verbose_name_plural = 'book categories'

    def get_url(self):
        return reverse('products_by_book_category', args=[self.slug])

    def __str__(self):
        return self.book_category


class FootwearCategory(models.Model):
    footwear_category = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'footwear category'
        verbose_name_plural = 'footwear categories'

    def get_url(self):
        return reverse('products_by_footwear_category', args=[self.slug])

    def __str__(self):
        return self.footwear_category
    
class ProvisionCategory(models.Model):
    provision_category = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'provision category'
        verbose_name_plural = 'provision categories'

    def get_url(self):
        return reverse('products_by_provision_category', args=[self.slug])

    def __str__(self):
        return self.provision_category
    


class ClothingCategory(models.Model):
    clothing_category = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'clothing category'
        verbose_name_plural = 'clothing categories'

    def get_url(self):
        return reverse('products_by_clothing_category', args=[self.slug])

    def __str__(self):
        return self.clothing_category
    

