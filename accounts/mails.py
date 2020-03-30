from django.conf import settings
from django.core.mail import send_mail


def send_contact_mail(data):
    """
    this function send subscribtion to you email with order
    """
    
    send_mail(
        f'New message from {data["email"]}',
        "You have new message",
        settings.FROM_EMAIL,
        ['tomaszcygal@yahoo.com'],
        fail_silently=False,
        
    )