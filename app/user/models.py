from django.db import models
from store.models import Store

class Group(models.Model):
    name = models.TextField(null= True)
    status = models.IntegerField(default = 0, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    name = models.TextField(null= True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    user_type = models.CharField(max_length=50, null=True)
    group = models.ForeignKey( Group, on_delete=models.SET_NULL, null=True)
    store = models.ForeignKey( Store, on_delete=models.SET_NULL, null=True)
    location = models.TextField(null= True)
    timezone = models.IntegerField(null = True)
    status = models.IntegerField(default = 0, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)