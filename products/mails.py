from django.core.mail import send_mail
from django.conf import settings



def send_subscribe_mail(data):
    """
    this function send subscribtion to you email with order
    """
    send_mail(
        f'Thank you for your subscribtion {data["email"]}',
        'You will be updated about our new products and promotions.',
        settings.FROM_EMAIL,
        [data["email"]],
        fail_silently=False,
    )



