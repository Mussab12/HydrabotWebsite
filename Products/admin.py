from email.headerregistry import Group
from django.contrib import admin
from .models import Product


from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(Product)

admin.site.unregister(Group)


