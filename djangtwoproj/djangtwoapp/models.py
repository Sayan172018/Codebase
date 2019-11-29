from django.db import models

# Create your models here.

class Users(models.Model):
    firstname=models.CharField(max_length=264,unique=True)
    lastname=models.CharField(max_length=264,unique=True)
    email=models.URLField(unique=True)
