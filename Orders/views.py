from django.shortcuts import render
from django.contrib import messages
from .models import Orders
from urllib import response
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate

from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from .models import OrderUpdate
import json

# Create your views here.
def orderItem(request):

    if request.method=='POST':
        items_json=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','')+" "+request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')
        
        order=Orders(items_json=items_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="The Order has been placed ")
        update.save()
        thank=True
        id=order.order_id
        return render(request,'checkout.html',{'thank':thank,'id':id})
    
    return render(request,'checkout.html') 

def orderUpdate(request):
    if request.method=="POST":
        orderId=request.POST.get('orderId','')
        email=request.POST.get('email','')
        
        try:
            order=Orders.objects.filter(order_id=orderId,email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=orderId)
                updates=[] 
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)

            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')     
    return render(request,'tracker.html')