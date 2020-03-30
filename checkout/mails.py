from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_checkout_mail(user, cart):

    """
    this function send confirmation email with order
    """
    html_message = render_to_string('order-confirmation.html', {'user': user, 'cart': cart})
    send_mail(
        "Subject here",
        f"Here is the message. {user.username}, {cart}",
        settings.FROM_EMAIL,
        [user.email],
        fail_silently=False,
        html_message=html_message
    )
