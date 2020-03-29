from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from products.mails import send_subscribe_mail

from .models import Product, ProductCategory


def all_products(request):
    if request.method == "POST":
        send_subscribe_mail(request.POST)
        messages.success(
            request, "Thank you for subscribtion. Check your mailbox."
        )
    products = Product.objects.all()
    name = request.GET.get("q")
    category_id = request.GET.get("category_id")
    if category_id:
        products = products.filter(category_id=category_id)

    if name:
        products = products.filter(name__icontains=name)

    page = request.GET.get("page", 1)
    products = products.order_by('name')
    paginator = Paginator(products, 8)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(
        request,
        "products.html",
        {
            "products": products,
            "categories": ProductCategory.objects.all(),
            "disable_background_image": True,
        },
    )


def product_details(request, id):
    product = Product.objects.get(id=id)
    return render(request, "product-details.html", {"product": product})
