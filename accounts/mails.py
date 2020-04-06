from django.conf import settings
from django.core.mail import send_mail


def send_contact_mail(request):
    """
    this function send subscribtion to you email with order
    """
    data = request.POST
    send_mail(
        f'New message from {data["email"]}',
        f"You have new message: {data['message']}\nFrom: {data['name']}",
        settings.FROM_EMAIL,
        ['tomaszcygal@yahoo.com'],
        fail_silently=False,
        
    )