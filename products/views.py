from django.shortcuts import render
from .models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def all_products(request):
    products= Product.objects.all()
    name= request.GET.get("q")
    category_id = request.GET.get("category_id")
    if category_id:
        products= products.filter(category_id= category_id)
        
    if name:
        products=products.filter(name__icontains= name)

    page = request.GET.get('page', 1)

    paginator = Paginator(products, 8)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products, "categories": ProductCategory.objects.all()})



def product_details(request, id):
    print('REQUEST: ', request)
    product = Product.objects.get(id=id)

    print('product: ', product)
    return render(request, 'product-details.html', {"product": product})

