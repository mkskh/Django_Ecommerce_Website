from django.shortcuts import render
from . import models


def home(request):
    products = models.Product.objects.all
    return render(request, 'ecommerce/home.html', {'products': products})


def about(request):
    return render(request, 'ecommerce/about.html')


def product_detail(request, id):
    product = models.Product.objects.get(pk=id)
    return render(request, 'ecommerce/product_detail.html', {'product': product})


