from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=264,unique=True)
    password=models.CharField(max_length=264,unique=True)
    email=models.EmailField(unique=True)
