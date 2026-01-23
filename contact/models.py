from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/', blank=True)

def __str__(self) -> str:
    return f"{self.first_name} {self.last_name}"