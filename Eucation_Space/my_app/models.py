from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    title_name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='media/', blank=True, null=True)
    price = models.CharField(max_length=100000)

    def __str__(self):
        return self.title_name