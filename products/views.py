from django.shortcuts import render
from .models import Product, ProductCategory

def all_products(request):
    print(request.GET)
    category_id= request.GET.get("category_id")
    if category_id:
        products= Product.objects.filter(category_id= category_id)
    else:
        products = Product.objects.all()
    return render(request, "products.html", {"products": products, "categories": ProductCategory.objects.all()})

