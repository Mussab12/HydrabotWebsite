
from email import message
import imp
from urllib import response
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate

from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.
# Function to get registeration page
def register(request):
    if request.method=='POST':
        # variables for getting the name,email and password
     username=request.POST['username']   
     first_name=request.POST['first_name']
     email=request.POST['email']
     Pass=request.POST['password1']
     Repass=request.POST['password2']
    #  Validation for form
     if (Pass==Repass):
      if User.objects.filter(username=username).exists():
         messages.info(request,'Username Exists')
         return redirect('register')
      elif(User.objects.filter(email=email).exists()):
         messages.info(request,'Email Exists')
         return redirect('register')
     
      elif(not username or not email or not Pass or not first_name):
         messages.info(request,'Please enter all fields')
         return redirect('register') 
      else:
         user=User.objects.create_user(username=username,password=Pass,first_name=first_name,email=email)
         user.save()
         print('user created')
         messages.success(request,'You have been registered successfully')
         return redirect('register')
         




       
        
     
     elif(Pass!=Repass):
      messages.info(request,'password not matching')
      return redirect('register') 

     

   
       
     
   
 
    else:
     return render(request,'registeration.html')


# Login
def login(request):
    if request.method=='POST':
        # variables for getting the name,email and password
       username=request.POST['username']   
       password1=request.POST['password']
       user=auth.authenticate(request,username=username,password=password1)
      #  if user is None:
      #    return render(request,'shop.html')
       if user is not None:
         auth.login(request,user)
         return redirect('/')
       
       else:
         messages.info(request,'Invalid credentials')
         return redirect('login')  

    else:
     return render(request,'shop.html')
   

def logout(request):
   auth.logout(request)
   return redirect('/')


