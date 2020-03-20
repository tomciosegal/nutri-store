from django.db import models

from django.contrib.auth.models import User


class Customer(models.Model):
    user=models.OneToOneField(User)
    full_name=models.CharField(max_length= 50)
    phone_number=models.CharField(max_length=16)
    country=models.CharField(max_length=20)
    postcode=models.CharField(max_length=10)
    town_city=models.CharField(max_length=20)
    street_address1=models.CharField(max_length=50)
    street_address2=models.CharField(max_length=50, null=True, blank=True)
    county=models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.email

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    total_cost = models.FloatField()
    shipment_address = models.TextField()
    status = models.IntegerField()
    delivery_type = models.IntegerField()

class OrderItem(models.Model):
     id = models.AutoField(primary_key=True)
     order_id = models.IntegerField()
     product_id = models.IntegerField()
     quantity = models.IntegerField()

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()

class CartItem(models.Model):
     id = models.AutoField(primary_key=True)
     cart_id = models.IntegerField()
     product_id = models.IntegerField()
     quantity = models.IntegerField()



