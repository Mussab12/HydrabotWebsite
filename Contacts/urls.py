from django.urls import path
from .import views
urlpatterns=[   

# path('contactme',views.Contact_us,name='contactme'),
path('Contact',views.Contact,name='Contact'),
]