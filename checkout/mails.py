from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from accounts.models import Customer
from products.models import Product


def send_checkout_mail(request):

    """
    this function send confirmation email with order
    """
    products = []
    for product_id, quantity in request.session['cart'].items():
        product = Product.objects.get(pk=product_id)
        products.append(product)
     
    context = {
        'user': request.user, 
        'total': request.session['total'], 
        'products': products,
        'customer' : Customer.objects.get(user=request.user)
    }
    html_message = render_to_string('order-confirmation.html', context)
    send_mail(
        "Thank You For Shopping at Nutristore",
        f"Here is the message. {request.user.username}",
        settings.FROM_EMAIL,
        [request.user.email],
        fail_silently=False,
        html_message=html_message
    )
