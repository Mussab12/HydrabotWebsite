from django.shortcuts import render



# from water_store.models import Products

# Create your views here.
# Function to get index page
def index(request): 
    # d1=Destination()
    # d1.price=1500
    return render(request, 'index.html')
# {'d1':d1}
# Function to get about page
def about(request):
    return render(request, 'about.html')


# Function to get product-details page


# Function to get login page
def shop(request):
    return render(request,'shop.html')   

# Function to get contactus page

def contact(request):
    
    return render(request,'contactus.html') 

def tracker(request):
    return render(request,'tracker.html')


