from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    descriptions = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    

class Keyword(models.Model):
    name = models.CharField(max_length=20)    

class Product(models.Model):
    name = models.CharField(max_length=50)
    product_category = models.ForeignKey(Category, on_delete=models.PROTECT) 
    descriptions = models.TextField()
    price = models.IntegerField()
    cover_file = models.ImageField()
    keywords = models.ManyToManyField(Keyword)
    added_by = models.ForeignKey(User, on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.name





 

