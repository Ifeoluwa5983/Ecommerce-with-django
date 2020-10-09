from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=300, null=True)
    email = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name


# class Category(models.Model):
#     title = models.CharField(max_length=300)
#     primaryCategory = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.title


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderItem = self.order_item_set.all()
        total = sum([item.get_total for item in orderItem])
        return total

    @property
    def get_cart_items(self):
        orderItem = self.order_item_set.all()
        total = sum([item.quantity for item in orderItem])
        return total


class Product(models.Model):
    mainImage = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=300)
    digital = models.BooleanField(default=False, null=True, blank=False)
    price = models.FloatField()

    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.mainImage.url
        except:
            url = ''
        return url


class Order_item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class Shipping_order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=300, null=True)
    state = models.CharField(max_length=300, null=True)
    city = models.CharField(max_length=300, null=True)
    zip_code = models.CharField(max_length=300, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
