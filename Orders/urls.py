from django.urls import path
from .import views
urlpatterns=[   

path('orderItem',views.orderItem,name='orderItem'),
path('orderUpdate',views.orderUpdate,name='orderUpdate')
]