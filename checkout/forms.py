from django import forms



class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2036)]

    credit_card_number = forms.IntegerField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)



class ShippingForm(forms.Form):
    full_name= forms.CharField(max_length=200)
    address_line_1=forms.CharField(max_length=200)
    address_line_2=forms.CharField(max_length=200, required= False)
    town_or_city=forms.CharField(max_length=30)
    postcode=forms.CharField(max_length=30)
