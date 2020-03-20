from django.shortcuts import render,redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, CustomerForm
from accounts.models import Customer
# Create your views here.


def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')

@login_required
def logout(request):
    """Log the user out"""
    username = ""
    if request.user.is_authenticated():
        username = request.user.username
    auth.logout(request)
    messages.success(request, f"You have been logged out {username}")
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated():
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            

            if user:
                auth.login(user=user, request=request)
                messages.success(request, f"You have successfully logged in {user.username}")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page
       will create a new user"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, f"You have successfully registered {user.username}")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})


def user_profile(request):
    """The user's profile page"""
    customer=Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            
            customer=form.save(commit=False)
            customer.user=request.user
            customer.save()
    else:
        form=CustomerForm(instance=customer)
    return render(request, 'profile.html', {"user": request.user, 'form': form})


def contact(request):
    if request.method == "POST":
        messages.success(request, "Thank You For Contatcting Us!")
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def delivery(request):
    return render(request, 'delivery.html')


def return_policy(request):
    return render(request, 'return-policy.html')
