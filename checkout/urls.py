from django.conf.urls import url
from .views import checkout, shipping

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^shipping/', shipping, name="shipping")
    ]
