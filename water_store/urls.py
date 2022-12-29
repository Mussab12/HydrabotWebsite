from unicodedata import name
from django.urls import path
from django.contrib import admin


from . import views

admin.site.site_header = 'Hydrabot-Store'
urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('shop',views.shop,name='shop'),
    path('tracker',views.tracker,name='tracker'),
    
   
    
  
    
    
    
    
]