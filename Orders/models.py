from django.db import models

# Create your models here.

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000,default="")
    name=models.CharField(max_length=90,default="")
    email=models.CharField(max_length=111,default="")
    address=models.CharField(max_length=111,default="")
    city=models.CharField(max_length=111,default="")
    state=models.CharField(max_length=111,default="")
    zip_code=models.CharField(max_length=111,default="")
    phone=models.CharField(max_length=111,default="")

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."