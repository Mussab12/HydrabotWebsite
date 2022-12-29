from django.urls import path
from .import views
urlpatterns=[
path('Product_details',views.Product_details,name='Product_details'),
path("allProducts/<int:myid>",views.allProducts,name='allProducts'),
path('Productcheckout',views.Productcheckout,name='Productcheckout'),



] 