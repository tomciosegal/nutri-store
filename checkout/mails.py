from django.core.mail import send_mail
from django.conf import settings



def send_checkout_mail(user, cart):
    send_mail(
        'Subject here',
        f'Here is the message. {user.username}, {cart}',
        settings.FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
    