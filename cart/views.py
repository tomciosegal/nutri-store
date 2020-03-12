from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from products.models import Product
from django.contrib import auth, messages

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    product = Product.objects.get(id= id)
    if quantity > product.quantity:
        messages.error(request, f"Only {product.quantity} availible")
        
        return redirect(reverse('index'))

    cart = request.session.get('cart', {})

    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    total = float(product.price) * quantity
    if request.session.get("total") :
        request.session["total"] += total

    else: 
        request.session["total"] = total
    

    

    return HttpResponse(1)


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))