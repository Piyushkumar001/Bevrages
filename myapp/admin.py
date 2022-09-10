from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Products)
# admin.site.register(Orders)
# admin.site.register(OrderDetails)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'pname', 'uom_id', 'price_per_unit', 'image')

@admin.register(Orders)
class ProductsAdmin(admin.ModelAdmin):
	list_display = ('id','customer_name', 'total', 'order_date')


@admin.register(OrderDetails)
class ProductsAdmin(admin.ModelAdmin):
	list_display = ('id', 'order_id', 'product_id', 'quantity', 'total_price')