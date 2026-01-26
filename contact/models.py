from django.db import models
from django.utils import timezone

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/', blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"