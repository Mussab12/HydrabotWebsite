from django.shortcuts import render
from django.contrib import messages
from .models import ContactModel
# Create your views here.
# def Contact_us(request):
#     # if request=='POST':
#     #     name=request.POST.get('name','')
#     #     email=request.POST.get('email','')
#     #     desc=request.POST.get('desc','')
#     #     print(name,email,desc)
#     return render(request,'aboutus.html')

def Contact(request):
    thank=False
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        desc=request.POST.get('desc','')
        print(name,email,desc)
        contact=ContactModel(name=name,email=email,desc=desc)
        contact.save()
        thank=True

    return render(request,'contactus.html',{'thank':thank})
