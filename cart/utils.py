from cart.models import Cart, CartItem


def load_cart(request, user):
    cart=Cart.objects.filter(user=user).first()
    if cart:
        request.session['cart'] = {}
        for item in CartItem.objects.filter(cart=cart):
            request.session['cart'][item.product_id] = item.quantity 