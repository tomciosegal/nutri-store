from accounts.forms import CustomerForm, UserLoginForm, UserRegistrationForm
from accounts.mails import send_contact_mail
from accounts.models import Customer
from cart.utils import load_cart
from checkout.models import Order
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, reverse


@login_required
def logout(request):

    """
    Logout the user
    """

    username = request.user.username
    auth.logout(request)
    messages.success(request, f"You have been logged out {username}")
    return redirect(reverse("index"))


def login(request):

    """
    Return a login page
    """

    if request.user.is_authenticated():
        return redirect(reverse("index"))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST["username"],
                password=request.POST["password"],
            )

            if user:
                auth.login(user=user, request=request)
                load_cart(request, user)
                messages.success(
                    request, f"You have successfully logged in {user.username}"
                )
                return redirect(reverse("index"))
            else:
                login_form.add_error(
                    None, "Your username or password is incorrect"
                )
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})


def registration(request):

    """
    View for users to register a new account.
    Checks if form is valid, and responds accordingly,
    then redirects users to the login page on successfully
    creating a new account.
    """

    if request.user.is_authenticated():
        return redirect(reverse("index"))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(
                username=request.POST["username"],
                password=request.POST["password1"],
            )
            if user:
                auth.login(user=user, request=request)

                messages.success(
                    request,
                    f"You have successfully registered {user.username}",
                )
                return redirect(reverse("index"))
            else:
                messages.error(
                    request, "Unable to register your account at this time"
                )
    else:
        registration_form = UserRegistrationForm()
    return render(
        request, "registration.html", {"registration_form": registration_form}
    )


def user_profile(request):

    """
    Renders profile page for user with a form to update
    their information. When posted creates a new customer.
    """

    customer = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            messages.success(request, "You have updated your profile")
    else:
        form = CustomerForm(instance=customer)
    has_order = False
    if customer:
        has_order = Order.objects.filter(customer=customer).exists()

    return render(
        request,
        "profile.html",
        {"user": request.user, "form": form, "has_order": has_order},
    )


def contact(request):
    if request.method == "POST":
        send_contact_mail(request)
        messages.success(request, "Thank You For Contatcting Us!")
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def delivery(request):
    return render(request, "delivery.html")


def return_policy(request):
    return render(request, "return-policy.html")


def subscribe_mail(request, mail):
    messages.success(request, "Thank You For Subscription")
    return redirect(reverse("index"))
