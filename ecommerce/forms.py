from django import forms
from .models import Category


class SearchForm(forms.Form):

    category_choices = [(category.id, category.name) for category in Category.objects.all()]
    category_choices.insert(0, ("", "All Categories")) 

    product_name = forms.CharField(required=False)
    category = forms.ChoiceField(choices=category_choices, widget=forms.Select, required=False)
    price_min = forms.DecimalField(required=False)
    price_max = forms.DecimalField(required=False)
