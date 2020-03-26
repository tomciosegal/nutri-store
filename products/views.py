from django.shortcuts import render
from .models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from products.mails import send_subscribe_mail
from django.contrib import messages


def all_products(request):
    if request.method == 'POST':
        send_subscribe_mail(request.POST)
        messages.success(request, "Thank you for subscribtion. Check your mailbox.")
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
    product = Product.objects.get(id=id)
    return render(request, 'product-details.html', {"product": product})

