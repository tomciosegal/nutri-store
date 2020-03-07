from django.shortcuts import render
from .models import Product, ProductCategory


def all_products(request):

    category_id = request.GET.get("category_id")
    if category_id:
        products= Product.objects.filter(category_id= category_id)
        print('products: ', products)
    else:
        products = Product.objects.all()
    return render(request, "products.html", {"products": products, "categories": ProductCategory.objects.all()})


def product_details(request, id):
    print('REQUEST: ', request)
    product = Product.objects.get(id=id)

    print('product: ', product)
    return render(request, 'product-details.html', {"product": product})
