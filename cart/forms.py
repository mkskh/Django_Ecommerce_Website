from django import forms
from .models import Cart
from user.models import UserProfile


class QuantityForm(forms.Form):

    quantity = forms.IntegerField()


class ShippingInfoForm(forms.ModelForm):
    password = None
    phone = forms.CharField(required=False, label="Phone", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
    address = forms.CharField(required=False, label="Address", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
    additional_address = forms.CharField(required=False, label="Additional Address", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
    city = forms.CharField(required=False, label="City", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
    region = forms.CharField(required=False, label="Region", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
    zip_code = forms.CharField(required=False, label="Zip Code", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
    country = forms.CharField(required=False, label="Country", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))

    class Meta:
        model = UserProfile
        exclude = ['user_id', 'date_of_modified', 'user']