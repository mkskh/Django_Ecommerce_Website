from django.shortcuts import render, get_object_or_404
from . import models
from cart.models import Cart


def custom_context(request):
    '''pass Category to base.html for populating Category nav section'''
    categories = models.Category.objects.all()
    if request.user.is_authenticated:
        quantity_cart = Cart.objects.filter(user=request.user).count()
    else:
        quantity_cart = 0
    return {'categories': categories, "quantity_cart": quantity_cart}


def home(request):
    products = models.Product.objects.all
    return render(request, 'ecommerce/home.html', {'products': products})


def about(request):
    return render(request, 'ecommerce/about.html')


def product_detail(request, id):
    product = models.Product.objects.get(pk=id)
    return render(request, 'ecommerce/product_detail.html', {'product': product, "product_id": id})


def get_by_category(request, category_name):
    category = models.Category.objects.get(name__iexact=category_name)
    products = models.Product.objects.filter(category=category)
    return render(request, 'ecommerce/get_by_category.html', {'products': products})



