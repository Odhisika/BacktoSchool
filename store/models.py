from django.db import models
from category.models import Category, BookCategory, ProvisionCategory, FootwearCategory, ClothingCategory 
from django.urls import reverse
from accounts.models import Account
from django.db.models import Avg, Count
import datetime



# Base Product Model (Now Concrete)

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=5000, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

    def averageReview(self):
        reviews = self.reviews.filter(status=True).aggregate(average=Avg('rating'))
        return float(reviews['average']) if reviews['average'] else 0

    def countReview(self):
        reviews = self.reviews.filter(status=True).aggregate(count=Count('id'))
        return int(reviews['count']) if reviews['count'] else 0


# Specific Product Models
class Book(Product):
    author = models.CharField(max_length=255)
    publication_date = models.DateField(default=datetime.date.today)
    book_category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, related_name="books", null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)


class Electronics(Product):
    brand = models.CharField(max_length=255)
    warranty_period = models.IntegerField(help_text="Warranty period in months")


class Size(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class FootSize(models.Model):
    number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.number) 


class Color(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name



class Footwear(Product):
    footwear_category = models.ForeignKey(FootwearCategory, on_delete=models.CASCADE, related_name="footwear", default=1)
    shoe_type = models.CharField(max_length=50)
    colors = models.ManyToManyField(Color, blank=True, related_name='footwears')
    footsizes = models.ManyToManyField(FootSize, blank=True, related_name='footwears')


class Clothing(Product):
    clothing_category = models.ForeignKey(ClothingCategory, on_delete=models.CASCADE, related_name="clothing", default=1)
    colors = models.ManyToManyField(Color, blank=True, related_name='clothings')
    sizes = models.ManyToManyField(Size, blank=True, related_name='clothings')




class Stationary(Product):
    brand = models.CharField(max_length=255)
    pack_size = models.IntegerField(help_text="Number of items in a pack")

class Provisions(Product):
    brand = models.CharField(max_length=255)
    provision_category = models.ForeignKey(ProvisionCategory, on_delete=models.CASCADE, related_name="provisions", default=1)
    pack_size = models.IntegerField(help_text="Number of items in a pack")
    colors = models.ManyToManyField(Color, blank=True, related_name='provisions')
    



class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="reviews")
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject if self.subject else "Review"



class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to='store/products', max_length=255)

    def __str__(self):
        return f"Image for {self.product.product_name}"

    class Meta:
        verbose_name = 'Product Gallery'
        verbose_name_plural = 'Product Galleries'
