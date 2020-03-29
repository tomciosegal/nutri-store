from cart.models import Cart, CartItem
from products.models import Product


def load_cart(request, user):
    cart=Cart.objects.filter(user=user).first()
    if cart:
        if not request.session.get('cart'):
            request.session['cart'] = {}
        for item in CartItem.objects.filter(cart=cart):
            request.session['cart'][item.product_id] = item.quantity 
            product=Product.objects.filter(pk=item.product_id).first()
            if request.session.get('total') and product:
                request.session['total'] += item.quantity * float(product.price)
            else:
                request.session['total'] = item.quantity * float(product.price)
        total_after_discount=0
        if request.session.get('total')  and request.session.get('total') > 50:
            total_after_discount = round(float(request.session.get('total')) * 0.9, 2)
        elif request.session.get('total'):
            total_after_discount = round(float(request.session.get('total')), 2)
        request.session['total_after_discount']=total_after_discount

def clear_cart(user):
    cart=Cart.objects.filter(user=user).delete()

