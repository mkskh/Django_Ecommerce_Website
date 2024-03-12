from django.shortcuts import render
from . import models


def home(request):
    products = models.Product.objects.all
    return render(request, 'ecommerce/home.html', {'products': products})


