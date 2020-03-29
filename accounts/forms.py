from accounts.models import Customer
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """Form to be used to log users in"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]

    def clean_email(self):
        """Form validation. Allows us to perform additional validation
            on our forms so we can customise the feedback that we
            give to our users"""

        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(" Your email address must be unique")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")

        if password1 != password2:
            raise ValidationError("Passwords must match")

        return password2


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "full_name",
            "phone_number",
            "postcode",
            "town_city",
            "street_address1",
            "street_address2",
            "county",
        ]
