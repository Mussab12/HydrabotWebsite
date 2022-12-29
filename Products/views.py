from django.shortcuts import render

from Products.models import Product


# Create your views here.
# Function to get Product-details page
def Product_details(request):
    prods=Product.objects.all() #this will fetch the data from the database
    return render(request,'product-details.html',{'prods':prods})


def allProducts(request,myid):
    #  Fetching the product using id
    product=Product.objects.filter(id=myid)
    
    return render(request,'prodview.html',{'product':product[0]})

def Productcheckout(request):
    return render(request,'checkout.html')




