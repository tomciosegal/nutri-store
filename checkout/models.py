from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class TimestampedModel(models.Model):
    """
    this model will post order to admin databse with order history
    """
    class Meta : 
        abstract= True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


class OrderHistory(TimestampedModel):
    """
    this model holds the user order history 
    """
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    total_cost = models.DecimalField(decimal_places=2, max_digits=6 )

    


class OrderItemHistory(TimestampedModel):

    """
    this model holds the user order history item
    """
    order_history = models.ForeignKey(OrderHistory, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
