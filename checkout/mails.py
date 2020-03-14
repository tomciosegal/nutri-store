from django.core.mail import send_mail



def send_checkout_mail():
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    