from django.contrib import admin
from .models import *

admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Shipping_order)
admin.site.register(Order_item)
admin.site.register(Product)

# Register your models here.
