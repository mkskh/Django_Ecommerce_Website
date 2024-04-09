from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart
from .forms import QuantityForm
from ecommerce.models import Product
from django.http import HttpResponseRedirect


@login_required
def add_to_cart(request, product_id):

    if request.method == 'POST':
        '''Add item(s) to the shopping card pressing button from product detail page'''
        product = Product.objects.get(id=product_id)
        cart_item = Cart.objects.filter(user=request.user, product=product).first()

        quantity = request.POST.get('quantity')

        if cart_item:
            #if product already exists
            cart_item.quantity = cart_item.quantity + int(quantity)
            cart_item.save()
            messages.success(request, 'Item added to your cart')

        else:
            #if product still not exists
            cart_item = Cart.objects.create(user=request.user, product=product)
            cart_item.quantity = int(quantity)
            cart_item.save()
            messages.success(request, 'Item added to your cart')

    elif request.method == 'GET':
        '''Add item to the shopping card pressing button from main page (quantity always 1)'''

        product = Product.objects.get(id=product_id)
        cart_item = Cart.objects.filter(user=request.user, product=product).first()

        if cart_item:
            #if product already exists
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
            messages.success(request, 'Item added to your cart')

        else:
            #if product still not exists
            Cart.objects.create(user=request.user, product=product)
            messages.success(request, 'Item added to your cart')
        
    referer = request.META.get('HTTP_REFERER')
    
    return HttpResponseRedirect(referer)


def add_to_cart_unknown_user(request):

    messages.success(request, 'To add a product to the shopping cart please sign in.')
    
    referer = request.META.get('HTTP_REFERER')
    
    return HttpResponseRedirect(referer)


@login_required
def cart_details(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.quantity * item.product.price for item in cart_items)

    return render(request, "cart/cart_details.html", {"cart_items": cart_items, "total_price": total_price})


@login_required
def update_cart_item(request, cart_item_id):

    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        if request.method == "POST":    

            new_quantity = request.POST.get('quantity')
            if new_quantity.isdigit() and int(new_quantity) > 0:
                cart_item.quantity = int(new_quantity)
                cart_item.save()
                messages.success(request, "Cart item quantity updated successfully")
            else:
                messages.error(request, "Invalid quantity value")
    
    return redirect('cart:cart_details')


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")

    return redirect("cart:cart_details")