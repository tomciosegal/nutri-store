from django.db import models
from products.models import Product
from accounts.models import Customer


class TimestampedModel(models.Model):
    """
    this model will post order to admin databse with order history
    """
    class Meta : 
        abstract= True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


class Order(TimestampedModel):
    """
    this model holds the user order history 
    """

    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    total_cost = models.DecimalField(decimal_places=2, max_digits=6 )

    


class OrderItem(TimestampedModel):

    """
    this model holds the user order history item
    """
    order_history = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
