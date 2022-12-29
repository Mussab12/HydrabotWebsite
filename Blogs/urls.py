from django.urls import path
from .import views
urlpatterns=[   

path("myBlog/<int:id>",views.myBlog,name='myBlog'),
path('Blogview',views.Blogview,name='Blogview')
]