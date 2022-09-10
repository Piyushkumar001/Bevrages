from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Products(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    pname = models.CharField(max_length = 100)
    description = models.TextField()
    uom_id = models.IntegerField(null= True)
    price_per_unit = models.DecimalField(max_digits = 5, decimal_places = 2)
    image = models.ImageField(upload_to = "images", null = True)

class Orders(models.Model):
	customer_name = models.ForeignKey(User, on_delete = models.CASCADE)
	total = models.DecimalField(max_digits = 5, decimal_places = 2)
	order_date = models.DateTimeField(auto_now_add = True)


class OrderDetails(models.Model):
	order_id = models.ForeignKey(Orders, on_delete = models.CASCADE)
	product_id = models.ForeignKey(Products, on_delete = models.CASCADE)
	quantity = models.PositiveIntegerField(default = 1)
	total_price = models.DecimalField(max_digits = 5, decimal_places = 2)

	def __str__(self):
		return str(self.order_id)