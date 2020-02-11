from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    category_id = models.IntegerField()
    quantity = models.IntegerField()

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



