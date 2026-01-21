from django.utils import timezone
from django.db import models

first_name = models.CharField(max_length=30)
last_name = models.CharField(max_length=30)
email = models.EmailField(max_length=254, blank=True)
category = models.CharField(max_length=50)
created_date = models.DateTimeField(default=timezone.now)
description = models.TextField(blank=True)
show = models.BooleanField(blank=True)
picture = models.ImageField(upload_to='images/%Y/%m/', blank=True)

def __str__(self) -> str:
    return f"{self.first_name} {self.last_name}"

class Contact(models.Model):
    first_name = first_name
    last_name = last_name
    email = email
    category = category
    created_date = created_date
    description = description
    picture = picture
    show = show