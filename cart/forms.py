from django import forms
from .models import Cart


class QuantityForm(forms.Form):

    quantity = forms.IntegerField()

