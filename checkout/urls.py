from django.conf.urls import url

from .views import checkout, order_history, shipping

urlpatterns = [
    url(r"^$", checkout, name="checkout"),
    url(r"^shipping/", shipping, name="shipping"),
    url(r"^order_history/", order_history, name="order_history"),
]
