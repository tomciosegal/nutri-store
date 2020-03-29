from django.conf import settings
from django.core.mail import send_mail


def send_checkout_mail(user, cart):

    """
    this function send confirmation email with order
    """
    send_mail(
        "Subject here",
        f"Here is the message. {user.username}, {cart}",
        settings.FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
