from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
from cart.models import Cart
from .forms import SearchForm


def custom_context(request):
    '''pass Category to base.html for populating Category nav section'''
    categories = models.Category.objects.all()
    if request.user.is_authenticated:
        quantity_cart = Cart.objects.filter(user=request.user).count()
    else:
        quantity_cart = 0
    return {'categories': categories, "quantity_cart": quantity_cart}


def home(request):

    products = models.Product.objects.order_by("-price")
    prod_total = products.count()

    paginator = Paginator(products, 20) # show 20 products per page

    page_number = request.GET.get("page")


    if request.method == "GET":

        category = False # for keeping chosen category in the field after clicking Search
        form = SearchForm()

        try:
            paginated_products = paginator.page(page_number)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            paginated_products = paginator.page(1)

        return render(request, 'ecommerce/home.html', {'products': paginated_products, 'form': form, "prod_total": prod_total, "category": category})

    elif request.method == "POST":
        form = SearchForm(request.POST)
        category = False

        product_name = request.POST["product_name"]
        category = request.POST["category"]
        price_min = request.POST["price_min"]
        price_max = request.POST["price_max"]
        
        if category:
            category_name = models.Category.objects.get(pk=category)
            products = products.filter(category=category_name)
            category = {"id": int(category), "name": category_name}
            print(category)
        
        if product_name:
            products = products.filter(product_name__icontains=product_name)

        if price_min:
            products = products.filter(price__gte=price_min)
        
        if price_max:
            products = products.filter(price__lte=price_max)
            
    return render(request, 'ecommerce/home.html', {'products': products, 'form': form, "prod_total": prod_total, "category": category})


def about(request):
    return render(request, 'ecommerce/about.html')


def product_detail(request, id):
    product = models.Product.objects.get(pk=id)
    return render(request, 'ecommerce/product_detail.html', {'product': product, "product_id": id})


def get_by_category(request, category_name):
    category = models.Category.objects.get(name__iexact=category_name)
    products = models.Product.objects.filter(category=category)
    return render(request, 'ecommerce/get_by_category.html', {'products': products})


