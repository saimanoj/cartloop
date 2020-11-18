from django.db import models

class Store(models.Model):
    name = models.TextField(null= True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)    
    location = models.TextField(null= True)
    timezone = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)