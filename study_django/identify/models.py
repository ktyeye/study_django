from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.db import models

# Create your models here.

 
class User(models.Model):
    userid = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    
    def __str__(self):
        return self.userid
    
class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    addr = models.CharField(max_length=100)
    email = models.EmailField()