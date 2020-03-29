from django.shortcuts import get_object_or_404
from products.models import Product, ProductCategory


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get("cart", {})

    cart_items = []
    total = 0
    product_count = 0
    total_after_discount = 0

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({"id": id, "quantity": quantity, "product": product})

    if total and total > 50:
        total_after_discount = round(float(total) * 0.9, 2)
    elif total:
        total_after_discount = round(float(total), 2)
    request.session["total_after_discount"] = total_after_discount
    diference = round(float(total) - total_after_discount, 2)

    return {
        "cart_items": cart_items,
        "total": total,
        "product_count": product_count,
        "total_after_discount": total_after_discount,
        "categories": ProductCategory.objects.all(),
        "diference": diference,
    }
