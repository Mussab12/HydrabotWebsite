from operator import mod
from django.db import models


# Create your models here.
# Product model
class Product(models.Model):
    Prod_id=models.AutoField
    Prod_title = models.CharField(max_length=200)
    Prod_price=models.IntegerField()
    Prod_img=models.ImageField(upload_to='pics')
    Prod_desc=models.CharField(max_length=300)


# class Blogpost(models.Model):
#     post_id=models.AutoField(primary_key=True)
#     title = models.CharField(max_length=200)
#     head0 = models.CharField(max_length=500,default="")
#     chead0 = models.CharField(max_length=500,default="")
#     head1 = models.CharField(max_length=500,default="")
#     chead1= models.CharField(max_length=500,default="")
#     head2 = models.CharField(max_length=500,default="")
#     chead2= models.CharField(max_length=500,default="")
#     pub_date=models.DateField()
#     thumbnail=models.ImageField(upload_to='pics')
#     def __str__(self):
#         return self.title