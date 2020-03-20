from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe
from checkout.mails import send_checkout_mail
from checkout.utils import create_order_history
from accounts.models import Customer
from checkout.forms import ShippingForm
from accounts.forms import CustomerForm

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    """The view will render the html page and 
        pass in forms and contents of the cart
        Links up the backend data to the frontend 
        user interface
    """
    customer=Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        customer_form = CustomerForm(request.POST, instance=customer)
        payment_form = MakePaymentForm(request.POST)
        if  customer_form.is_valid() and payment_form.is_valid():
            customer=customer_form.save(commit=False)
            customer.user=request.user
            customer.save()
        
            # cart = request.session.get('cart', {})
            # total = 0
            # for id, quantity in cart.items():
            #     product = get_object_or_404(Product, pk=id)
            #     total += quantity * product.price
            #     order_line_item = OrderLineItem(
            #         order=order,
            #         product=product,
            #         quantity=quantity
            #     )
            #     order_line_item.save()

            if total < 60:
                total = total + shipping
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                # send_checkout_mail(request.user, request.session['cart'])
                create_order_history(request.user, request.session)
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                request.session['total'] = 0
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = CustomerForm(instance=customer)
    
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})


def shipping(request):
    customer=Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer=form.save(commit=False)
            customer.user=request.user
            customer.save()
            return redirect("checkout")
    else:
        form=CustomerForm(instance=customer)
    return render(request, 'shipping.html', {'customer': Customer.objects.filter(user=request.user).first(), 'form': form})

    # if request.method == "POST":
    #     form=ShippingForm(request.POST)
    #     if not form.is_valid():
    #         messages.error(request, f"Error occured: {form.errors}")
    #         return render(request, "shipping.html", {'customer': Customer.objects.filter(user=request.user).first()})
    #     return redirect("checkout")
    # return render(request, "shipping.html", {'customer': Customer.objects.filter(user=request.user).first()})

def order_confirmation(request):
    return ("order-confirmation.html")