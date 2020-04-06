from django.conf import settings
from django.core.mail import send_mail
from smtplib import SMTPAuthenticationError
from django.contrib import messages


def send_contact_mail(request):
    """
    this function send subscribtion to you email with order
    """
    data = request.POST
    try:
        send_mail(
            f'New message from {data["email"]}',
            f"You have new message: {data['message']}\nFrom: {data['name']}",
            settings.FROM_EMAIL,
            ['tomaszcygal@yahoo.com'],
            fail_silently=False,
        )
    except SMTPAuthenticationError:
        messages.error(request, "Your order confirmation email send failed")
    
    