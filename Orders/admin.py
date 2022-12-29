from django.contrib import admin
from .models import Orders
from .models import OrderUpdate
# Register your models here.
admin.site.register(Orders)
admin.site.register(OrderUpdate)