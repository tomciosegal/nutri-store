from checkout.models import TimestampedModel
from django.contrib.auth.models import User
from django.db import models


class Cart(TimestampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
