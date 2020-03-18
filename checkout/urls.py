from django.conf.urls import url
from .views import checkout, shipping, order_confirmation

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^shipping/', shipping, name="shipping"),
    url(r'^order_confirmation/',order_confirmation, name="order_confirmation" )
    ]
