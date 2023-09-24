from datetime import timezone
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, null=True, blank=True)
    category_image = models.ImageField(upload_to="category/")

    def __str__(self):
        return f"{self.category_name}"


class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.color_name}"


class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50, null=True, blank=True)
    product_year=models.IntegerField( null=True, blank=True)
    product_review=models.TextField(max_length=1000, null=True, blank=True)
    product_image=models.ImageField(upload_to="products/")
    product_comment = models.TextField(max_length = 1000, null=True, blank=True)
    product_color = models.ManyToManyField(Color, blank=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    product_interior1 = models.ImageField(upload_to="interior/", null=True, blank=True)
    product_interior2 = models.ImageField(upload_to="interior/", null=True, blank=True)

    def __str__(self):
        return f"{self.product_name}"
        
        

class Contact(models.Model):
    contact_name = models.CharField(max_length=50, null=True, blank=True)
    contact_surname = models.CharField(max_length=50, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_comment = models.TextField(max_length = 1000, null=True, blank=True)

    def __str__(self):
        return f"{self.contact_name}"

class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
      return f"{self.name}"