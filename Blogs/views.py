from django.shortcuts import render
from .models import Blogpost

# Create your views here.
def myBlog(request,id):
    posts=Blogpost.objects.filter(post_id=id)[0]
    print(posts)
    return render(request,'blog.html',{'posts':posts})


def Blogview(request):
    myposts=Blogpost.objects.all()
    print(myposts)
    return render(request,'blogmain.html',{'myposts':myposts})