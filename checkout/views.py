from smtplib import SMTPAuthenticationError

import stripe
from accounts.forms import CustomerForm
from accounts.models import Customer
from cart.utils import clear_cart
from checkout.mails import send_checkout_mail
from checkout.utils import create_order_history
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse
from products.models import Product

from .forms import MakePaymentForm
from .models import Order, OrderItem

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):

    """
    Renders checkout info page with navbar and
    footer removed to fit with conventions of online shops.
    Provides Stripe with the necessary keys to process
    payment when user clicks the "Submit Payment" button.
    """

    customer = None
    if request.user.is_authenticated():
        customer = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        payment_form = MakePaymentForm(request.POST)
        if payment_form.is_valid():

            cart = request.session.get("cart", {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price

            if total < 60:
                total = float(total) + 4.99
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data["stripe_id"],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                try:
                    send_checkout_mail(request)
                except SMTPAuthenticationError:
                    messages.error(
                        request, "Your order confirmation email send failed"
                    )
                create_order_history(request.user, request.session)
                clear_cart(request.user)
                messages.error(request, "You have successfully paid")
                request.session["cart"] = {}
                request.session["total"] = 0
                return redirect(reverse("products"))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(
                request, "We were unable to take a payment with that card!"
            )
    else:
        payment_form = MakePaymentForm()

    return render(
        request,
        "checkout.html",
        {
            "payment_form": payment_form,
            "publishable": settings.STRIPE_PUBLISHABLE,
            "disable_header": True,
            "disable_footer": True,
        },
    )


def shipping(request):

    """
    Renders checkout shipping page with navbar and footer
    removed to fit with conventions of online shops.
    If user not logged in getting to this stage is blocked,
    and user is asked to login.
    """

    customer = None
    if request.user.is_authenticated():
        customer = Customer.objects.filter(user=request.user).first()
    else:
        messages.error(request, "Need to be logged in to do checkout")
        return redirect(reverse("login"))
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            return redirect("checkout")
    else:
        form = CustomerForm(instance=customer)
    return render(
        request,
        "shipping.html",
        {
            "customer": customer,
            "form": form,
            "disable_header": True,
            "disable_footer": True,
        },
    )


def order_history(request):

    """
    Displays order history to the user listed
    by date of purchase.
    """

    customer = None
    if request.user.is_authenticated():
        customer = Customer.objects.filter(user=request.user).first()
    orders = []
    if customer:
        orders = Order.objects.filter(customer=customer).order_by(
            "-created_at"
        )
    orders_with_items = []
    for order in orders:
        order_items = OrderItem.objects.filter(order_history=order)
        orders_with_items.append({"order": order, "items": order_items})
    return render(request, "order_history.html", {"orders": orders_with_items})


def order_confirmation(request):
    return render(request, "order-confirmation.html")
