from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_subscribe_mail(data):
    """
    this function send subscribtion to you email with order
    """

    html_message = render_to_string(
        "subscribe_mail.html", {"mail": data["email"]}
    )
    send_mail(
        f'Thank you for your subscribtion {data["email"]}',
        "You will be updated about our new products and promotions.",
        settings.FROM_EMAIL,
        [data["email"]],
        fail_silently=False,
        html_message=html_message,
    )
