from django.db import models

# Create your models here.
class ContactModel(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)   
    email=models.CharField(max_length=70,default="")
    desc=models.CharField(max_length=5000,default="")

