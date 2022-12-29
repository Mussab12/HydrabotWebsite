from django.db import models

# Create your models here.
class User(models.Model): # converting class to model 
    Name=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Password=models.CharField(max_length=150)    


    